#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> board;
int TURN = 0;
board BOARD = {-1, 2,2,2, 2,2,2, 2,2,2};  


int MAGIC[10] = {-1,
    8,1,6,
    3,5,7,
    4,9,2
};

void printBoard();


int Posswin(char p){
    int target = (p == 'X') ? 3 : 5;  
    vector<int> playerMoves;
    int blank = 0;

    for(int i=1;i<=9;i++){
        if(BOARD[i] == target) playerMoves.push_back(MAGIC[i]);
    }


    for(int i=1;i<=9;i++){
        if(BOARD[i] == 2){
            for(size_t a=0;a<playerMoves.size();a++){
                for(size_t b=a+1;b<playerMoves.size();b++){
                    if(playerMoves[a] + playerMoves[b] + MAGIC[i] == 15){
                        return i; 
                    }
                }
            }
        }
    }
    return 0;
}

void Go(int n){
    if(BOARD[n] != 2){
        cout<<"Invalid move"<<endl;
        return;
    }
    ++TURN;
    if(TURN % 2 != 0)
        BOARD[n] = 3;   
    else
        BOARD[n] = 5;   
}

void playMagic(){

    if(BOARD[5] == 2) Go(5);
    else Go(1);
    printBoard();

    for(int turn=2;turn<=9;turn++){
        int move = 0;

        if(Posswin((TURN % 2 != 0) ? 'X':'O'))
            move = Posswin((TURN % 2 != 0) ? 'X':'O');
        else if(Posswin((TURN % 2 != 0) ? 'O':'X'))
            move = Posswin((TURN % 2 != 0) ? 'O':'X');
        else{
            for(int i=1;i<=9;i++){
                if(BOARD[i] == 2){
                    move = i;
                    break;
                }
            }
        }

        Go(move);
        printBoard();
    }
}

void printBoard(){
    for(int i=1;i<=9;i++){
        if(BOARD[i] == 3) cout<<'X';
        else if(BOARD[i] == 5) cout<<'O';
        else cout<<' ';
        
        if(i==3 || i==6) cout<<"\n---------\n";
        else if(i!=9) cout<<" | ";
    }
    cout<<"\n\n";
}

int main(){
    playMagic();
    return 0;
}
