#include<iostream>
#include<vector>
#include<string>
#include<list>

using namespace std;

// costanti
const int gridsize = 10;
const char ship = '#', hit = 'H', miss = 'M', water = '~';

// Inizializzazione della board
void InitializedBoard(vector<vector<char>> &board){
    board.clear(); // resetta la board se chiamata più volte

    for(int i = 0; i < gridsize; i++){
        vector<char> row(gridsize,water);
        board.push_back(row);
    }
} 

// Stampa la board
void PrintBoard(const vector<vector<char>> &board){
    cout << "  ";
    // stampa i numeri
    for(int i = 0; i < gridsize; i++){
        cout << i << " ";
    }
    cout << endl;
    // stampa la griglia con il simbolo dell'acqua
    for(int i = 0; i < gridsize; i++){
        cout << i << " ";
        for(int j = 0; j < gridsize; j++){
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Creazione della nave
bool placeShips(vector<vector<char>> &board, int x, int y, int size, char direction) {
    if (direction == 'H') { // Orizzontale
        if (y + size > gridsize) return false;
        for (int i = 0; i < size; i++) {
            if ((board[x][y + i] != water) || (board[x][y + i] == ship)) return false; 
        }
        for (int i = 0; i < size; i++) {
            board[x][y + i] = ship; // Posiziona la nave
        }
    } else if (direction == 'V') { // Verticale
        if (x + size > gridsize) return false;
        for (int i = 0; i < size; i++) {
            if ((board[x + i][y] != water) || (board[x + i][y] == ship)) return false;
        }
        for (int i = 0; i < size; i++) {
            board[x + i][y] = ship; 
        }
    } else {
        return false;
    }
    return true;
}

//Gestione casella colpita
bool IsHit(vector<vector<char>> &board, int x, int y){
    if(board[x][y] == ship){
        board[x][y] = hit;
        return true;
    }else if(board[x][y] == water){
        board[x][y] = miss;
        return false;
    }
    // se già colpito non fare nulla
    return false;
}

//Gestione nave distrutta
bool IsSunk(vector<vector<char>> &board, int x, int y, int size, char direction){
    if (direction == 'H') { // Orizzontale
        for (int i = 0; i < size; i++) {
            if (board[x][y + i] != hit) return false; // verifica se tutte le caselle sono colpite
        }
    } else if (direction == 'V') { // Verticale
        for (int i = 0; i < size; i++) {
            if (board[x + i][y] != hit) return false; // 
        }
    } else {
        return false;
    }
    return true;
}

// func per la direzione delle navi  H V
char direction(char dir){
    cout << "Dimmi se vuoi posizionare la nave orizzontalmente (H) o verticalmente (V): ";
    do
    {
        cin >> dir;
    } while (dir != 'H' && dir != 'V');
    return dir;
}

// func per la cordinata X
int cordinateX(int cordX){
    cout << "Inserisci la cordinata X: ";
    do
    {
        if(cordX < 0 || cordX >= gridsize){
            cout << "Inserisci una coordinata X valida (0-" << gridsize - 1 << ")." << endl;
        }
        cin >> cordX;
    } while (cordX < 0 || cordX >= gridsize);
    return cordX;
}

// func per la cordinata Y
int cordinateY(int cordY){
    cout << "Inserisci la cordinata Y: ";
    do
    {
        if(cordY < 0 || cordY >= gridsize){
            cout << "Inserisci una coordinata Y valida (0-" << gridsize - 1 << ")." << endl;
        }
        cin >> cordY;
    } while (cordY < 0 || cordY >= gridsize);
    return cordY;
}

// func per verifcare se tutte le navi della board sono affondate
bool allShipsSunk(vector<vector<char>> &board){
    for(int i = 0; i < gridsize; i++){
        for(int j = 0; j < gridsize; j++){
            if(board[i][j] == ship){
                return false; // c'è ancora una nave non affondata
            }
        }
    }
    return true; // tutte le navi sono affondate 
}