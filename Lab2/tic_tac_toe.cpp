#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> board;
int TURN = 0;
board BOARD = {-1,
    2,2,2,
    2,2,2,
    2,2,2
};

void printBoard();

int checkRows(int n){
    int product = 1;
    int blank = 0;
    for(int i = 1; i <= 7; i += 3){
        for(int j = i ; j < i+3; j++){
            if(BOARD[j] == 2)
                blank = j;
            product *= BOARD[j];
        }
        // cout<<"ROWS: "<<i<< " :"<<product<<endl;

        if(product == n && blank != 0)
            return blank;    
        product = 1;       
    }

    return 0 ;
}

int checkColumns(int n){
    int product = 1;
    int blank = 0;
    for(int i = 1; i <= 3; i++){
        for(int j = i ; j < i+7; j += 3){
            if(BOARD[j] == 2)
                blank = j;
            product *= BOARD[j];
        }
        // cout<<"COLS: "<<i<< " :"<<product<<endl;

        if(product == n && blank != 0)
            return blank;     
        product = 1;        
    }
    return 0;
}

int checkDiagonal(int n){
    int product = 1;
    int blank = 0;
    for(int i = 1; i<=9; i += 4){
        if(BOARD[i] == 2)
                blank = i;
        product *= BOARD[i];
        
    }
    if(product == n && blank != 0)
            return blank;

    


    product = 1;
    blank = 0;
    for(int i = 3; i<= 7; i+= 2){
        if(BOARD[i] == 2)
                blank = i;
        product *= BOARD[i];
    }
    if(product == n && blank != 0)
            return blank;


    return 0;
}

int checkWing(int n){
    int row = checkRows(n);
    
    if(row != 0)
        return row;
    
    
    int cols = checkColumns(n);
    if(cols != 0)
        return cols;
    
    
    int diag = checkDiagonal(n);
    if(diag != 0)
        return diag;

    return 0;
}

int Make2(){
    if(BOARD[5] == 2)
        return 5;
    else if(BOARD[2] == 2)
        return 2;
    else if(BOARD[4] == 2)
        return 4;
    else if(BOARD[6] == 2)
        return 6;
    else if(BOARD[8] == 2)
        return 8;
    
    return 0;
}

int Posswin(char p){
    if(p == 'X')
        return checkWing(18);
    return checkWing(50);
}


void Go(int n){
    if(BOARD[n] != 2){
        cout<<"Invalid move";
        return;
    }

    ++TURN;
    
    if(TURN % 2 != 0)
        BOARD[n] = 3;
    else
        BOARD[n] = 5;
}

void playOdd(){

    // 1
    Go(1); 
    printBoard();

    //2
    if(BOARD[5] == 2)
        Go(5);
    else
        Go(1);
    printBoard();

    
    // 3
    if(BOARD[9] == 2)
        Go(9);
    else
        Go(3);

    printBoard();
    //4
    if(Posswin('X')){
        Go(Posswin('X'));
    }
    else
        Go(Make2());


    printBoard();
    //5
    if(Posswin('X')){
        Go(Posswin('X'));
    }else if(Posswin('O')){
        Go(Posswin('O'));
    }else if(BOARD[7] != 2){
        Go(7);
    }else{
        Go(3);
    }
    printBoard();
    //6
    if(Posswin('O'))
        Go(Posswin('O'));
    else if(Posswin('X'))
        Go(Posswin('X'));
    else 
        Go(Make2());
    printBoard();
    //7
    if(Posswin('X')){
        Go(Posswin('X'));
    }else if(Posswin('O')){
        Go(Posswin('O'));
    }else{
        for(int i = 1; i <=9; i++){
            if(BOARD[i] != 2){
                Go(i);
                break;
            }    
        }
    }

    printBoard();
    //8
    if(Posswin('O'))
        Go(Posswin('O'));
    else if(Posswin('X'))
        Go(Posswin('X'));
    else{
        for(int i = 1; i <=9; i++){
            if(BOARD[i] != 2){
                Go(i);
                break;
            }    
        }
    }
    printBoard();
    //9
    if(Posswin('X')){
        Go(Posswin('X'));
    }else if(Posswin('O')){
        Go(Posswin('O'));
    }else{
        for(int i = 1; i <=9; i++){
            if(BOARD[i] != 2){
                Go(i);
                break;
            }    
        }
    }


    
}

void printBoard(){
    for(int i = 1; i <=9 ; i++){
        if(BOARD[i] == 3)
            cout<<'X';
        else if(BOARD[i] == 5)
            cout<<'O';
        else 
            cout<<' ';
        
        
        if((i == 3 || i == 6))
            cout<<endl<<"---------"<<endl;
        else if(i != 9)
            cout<<" | ";
    }
    cout<<endl<<endl;
}


int main(){

    playOdd();
    


    return 0;
}


