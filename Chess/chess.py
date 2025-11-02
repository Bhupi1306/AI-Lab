import copy

# Piece values for evaluation
PIECE_VALUES = {
    'P': 100, 'N': 320, 'B': 330, 'R': 500, 'Q': 900, 'K': 20000,
    'p': -100, 'n': -320, 'b': -330, 'r': -500, 'q': -900, 'k': -20000
}

class ChessGame:
    def __init__(self):
        # Simplified 8x8 board - uppercase = white, lowercase = black
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.white_turn = True
    
    def print_board(self):
        print("\n  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(f"{8-i} {' '.join(row)} {8-i}")
        print("  a b c d e f g h\n")
    
    def is_valid_pos(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    
    def is_white(self, piece):
        return piece.isupper()
    
    def get_moves(self, row, col):
        """Get all valid moves for a piece at position"""
        piece = self.board[row][col]
        if piece == '.':
            return []
        
        moves = []
        is_white = self.is_white(piece)
        piece_type = piece.upper()
        
        if piece_type == 'P':  # Pawn
            direction = -1 if is_white else 1
            # Move forward
            if self.is_valid_pos(row + direction, col):
                if self.board[row + direction][col] == '.':
                    moves.append((row + direction, col))
            # Capture diagonally
            for dc in [-1, 1]:
                nr, nc = row + direction, col + dc
                if self.is_valid_pos(nr, nc):
                    target = self.board[nr][nc]
                    if target != '.' and self.is_white(target) != is_white:
                        moves.append((nr, nc))
        
        elif piece_type == 'N':  # Knight
            knight_moves = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
            for dr, dc in knight_moves:
                nr, nc = row + dr, col + dc
                if self.is_valid_pos(nr, nc):
                    target = self.board[nr][nc]
                    if target == '.' or self.is_white(target) != is_white:
                        moves.append((nr, nc))
        
        elif piece_type in ['B', 'R', 'Q']:  # Bishop, Rook, Queen
            directions = []
            if piece_type in ['B', 'Q']:  # Diagonal
                directions += [(-1,-1), (-1,1), (1,-1), (1,1)]
            if piece_type in ['R', 'Q']:  # Straight
                directions += [(-1,0), (1,0), (0,-1), (0,1)]
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                while self.is_valid_pos(nr, nc):
                    target = self.board[nr][nc]
                    if target == '.':
                        moves.append((nr, nc))
                    elif self.is_white(target) != is_white:
                        moves.append((nr, nc))
                        break
                    else:
                        break
                    nr += dr
                    nc += dc
        
        elif piece_type == 'K':  # King
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = row + dr, col + dc
                    if self.is_valid_pos(nr, nc):
                        target = self.board[nr][nc]
                        if target == '.' or self.is_white(target) != is_white:
                            moves.append((nr, nc))
        
        return moves
    
    def get_all_moves(self, is_white):
        """Get all possible moves for a player"""
        moves = []
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece != '.' and self.is_white(piece) == is_white:
                    piece_moves = self.get_moves(r, c)
                    for move in piece_moves:
                        moves.append(((r, c), move))
        return moves
    
    def make_move(self, from_pos, to_pos):
        """Make a move on the board"""
        fr, fc = from_pos
        tr, tc = to_pos
        self.board[tr][tc] = self.board[fr][fc]
        self.board[fr][fc] = '.'
        self.white_turn = not self.white_turn
    
    def evaluate(self):
        """Evaluate board position (positive favors white)"""
        score = 0
        for row in self.board:
            for piece in row:
                if piece in PIECE_VALUES:
                    score += PIECE_VALUES[piece]
        return score
    
    def is_game_over(self):
        """Check if game is over (simplified - just check if kings exist)"""
        has_white_king = any('K' in row for row in self.board)
        has_black_king = any('k' in row for row in self.board)
        return not (has_white_king and has_black_king)
    
    def minimax(self, depth, is_maximizing, alpha=float('-inf'), beta=float('inf')):
        """Minimax algorithm with alpha-beta pruning and depth limiting"""
        if depth == 0 or self.is_game_over():
            return self.evaluate(), None
        
        moves = self.get_all_moves(is_maximizing)
        if not moves:
            return self.evaluate(), None
        
        best_move = None
        
        if is_maximizing:
            max_eval = float('-inf')
            for move in moves:
                # Make move
                from_pos, to_pos = move
                temp_board = copy.deepcopy(self.board)
                
                self.board[to_pos[0]][to_pos[1]] = self.board[from_pos[0]][from_pos[1]]
                self.board[from_pos[0]][from_pos[1]] = '.'
                
                eval_score, _ = self.minimax(depth - 1, False, alpha, beta)
                
                # Undo move
                self.board = temp_board
                
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Beta cutoff
            
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in moves:
                # Make move
                from_pos, to_pos = move
                temp_board = copy.deepcopy(self.board)
                
                self.board[to_pos[0]][to_pos[1]] = self.board[from_pos[0]][from_pos[1]]
                self.board[from_pos[0]][from_pos[1]] = '.'
                
                eval_score, _ = self.minimax(depth - 1, True, alpha, beta)
                
                # Undo move
                self.board = temp_board
                
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Alpha cutoff
            
            return min_eval, best_move
    
    def get_ai_move(self, depth):
        """Get best move for current player using minimax"""
        _, best_move = self.minimax(depth, self.white_turn)
        return best_move


def parse_position(pos_str):
    """Convert chess notation (e.g., 'e2') to board indices"""
    col = ord(pos_str[0].lower()) - ord('a')
    row = 8 - int(pos_str[1])
    return row, col

def position_to_str(row, col):
    """Convert board indices to chess notation"""
    return f"{chr(col + ord('a'))}{8 - row}"


# Main game loop
def main():
    game = ChessGame()
    
    print("=" * 50)
    print("    Simple Chess Game with Minimax AI")
    print("=" * 50)
    
    # Choose color
    while True:
        color_choice = input("\nChoose your color (w/b): ").strip().lower()
        if color_choice in ['w', 'b']:
            player_is_white = (color_choice == 'w')
            break
        print("Invalid choice. Enter 'w' for White or 'b' for Black")
    
    # Choose difficulty (depth)
    print("\nSet AI difficulty by choosing search depth (1-20):")
    print("  Lower depth (1-3): Easier, faster moves")
    print("  Medium depth (4-6): Moderate challenge")
    print("  High depth (7-10): Very challenging")
    print("  Expert depth (11-20): Extremely difficult, slower computation")
    
    while True:
        try:
            depth = int(input("\nEnter depth (1-20): ").strip())
            if 1 <= depth <= 20:
                break
            print("Please enter a number between 1 and 20")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20")
    
    player_color = "White" if player_is_white else "Black"
    ai_color = "Black" if player_is_white else "White"
    
    print(f"\nGame starting!")
    print(f"You are playing as {player_color}")
    print(f"AI search depth: {depth}")
    print(f"\nEnter moves in format: e2 e3")
    print("-" * 50)
    
    move_count = 0
    
    while not game.is_game_over():
        game.print_board()
        
        current_player = "White" if game.white_turn else "Black"
        is_player_turn = (game.white_turn == player_is_white)
        
        if is_player_turn:
            print(f"Your turn ({player_color})")
            
            while True:
                try:
                    user_input = input("Enter move: ").strip().lower()
                    
                    if user_input == 'quit':
                        print("Game ended by player.")
                        return
                    
                    parts = user_input.split()
                    if len(parts) != 2:
                        print("Invalid input. Use format: e2 e4")
                        continue
                    
                    from_pos = parse_position(parts[0])
                    to_pos = parse_position(parts[1])
                    
                    # Validate move
                    piece = game.board[from_pos[0]][from_pos[1]]
                    if piece == '.':
                        print("No piece at that position!")
                        continue
                    if game.is_white(piece) != game.white_turn:
                        print("That's not your piece!")
                        continue
                    
                    valid_moves = game.get_moves(*from_pos)
                    if to_pos not in valid_moves:
                        print("Invalid move for that piece!")
                        continue
                    
                    game.make_move(from_pos, to_pos)
                    move_count += 1
                    break
                    
                except Exception as e:
                    print(f"Error: {e}. Try again.")
        
        else:
            print(f"AI's turn ({ai_color}) - Thinking...")
            move = game.get_ai_move(depth)
            
            if move:
                from_pos, to_pos = move
                print(f"AI moves: {position_to_str(*from_pos)} to {position_to_str(*to_pos)}")
                game.make_move(from_pos, to_pos)
                move_count += 1
            else:
                print("AI has no valid moves!")
                break
    
    game.print_board()
    print("=" * 50)
    print("              GAME OVER!")
    print("=" * 50)
    
    if not any('K' in row for row in game.board):
        winner = "Black"
    else:
        winner = "White"
    
    if winner == player_color:
        print(f"Congratulations! You ({player_color}) win!")
    else:
        print(f"AI ({ai_color}) wins! Better luck next time!")
    
    print(f"Total moves: {move_count}")


if __name__ == "__main__":
    main()