// librerie
#include<iostream>
#include<vector>
#include<string>
#include<list>
//
using namespace std;
// costanti
const int gridsize = 10;
const char ship = '#', hit = 'H', miss = 'M', water = '~';
// classi
class Ship{
    private:
        int size;
        int n_ships;
        int cord_x;
        int cord_y;
        int hp;
        char direction;
        string name;
    public:
        Ship(int size, int n_ships, int cord_x, int cord_y, int hp, char direction, string name)
        :size(size),n_ships(n_ships),cord_x(cord_x),cord_y(cord_y),hp(hp),direction(direction),name(name){}
        // getters
        int getSize()const{return size;}
        int getN_ships()const{return n_ships;}
        int getCord_x()const{return cord_x;}
        int getCord_y()const{return cord_y;}
        int getHP()const{return hp;};
        char getDirection()const{return direction;}
        string getName()const{return name;}
        //setters
        void setSize(int size){this->size=size;}
        void setN_ships(int n_ships){this->n_ships=n_ships;}
        void setCord_x(int cord_x){this->cord_x=cord_x;}
        void setCord_y(int cord_y){this->cord_y=cord_y;}
        void setHP(int hp){this->hp=hp;}
        void setDirection(char direction){this->direction=direction;}
        void setName(string name){this->name=name;}
};
// Inizializzazione della board
void InitializedBoard(vector<vector<char>> &board){
    for(int i = 0; i < gridsize; i++){
        vector<char> row(gridsize,water);
        board.push_back(row);
    }
} 
// Stampa la board
void PrintBoard(const vector<vector<char>> &board){
    cout << "  ";
    for(int i = 0; i < gridsize; i++){
        cout << i << " ";
    }
    cout << endl;
    //
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
        return true;
    }
    return true;
}
//Gestione nave distrutta
bool IsSunk(vector<vector<char>> &board, int x, int y, int size, char direction){
    if (direction == 'H') { // Orizzontale
        for (int i = 0; i < size; i++) {
            if (board[x][y + i] != hit) return false; // Verifica che la casella sia stata colpita, board[x][y + i] == hit return true
        }
    } else if (direction == 'V') { // Verticale
        for (int i = 0; i < size; i++) {
            if (board[x + i][y] != hit) return false; // Verifica che la casella sia stata colpita
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
    cout << "Inserisci la cordinata X: ";
    do
    {
        if(cordY < 0 || cordY >= gridsize){
            cout << "Inserisci una coordinata X valida (0-" << gridsize - 1 << ")." << endl;
        }
        cin >> cordY;
    } while (cordY < 0 || cordY >= gridsize);
    return cordY;
}
// metodo principale
int main(int argc, char const *argv[])
{
    // creazione oggetto nave
    Ship corazzata(4,1,0,0,4,'H',"Corazzata");
    Ship sottomarino(3,3,0,0,3,'H',"Sottomarino");
    Ship fregata(2,3,0,0,2,'H',"Fregata");
    Ship lancia(1,2,0,0,1,'H',"Lancia");
    vector<Ship*> ships = {&corazzata, &sottomarino, &fregata, &lancia}; // lista delle navi

    // dichiarazione delle variabili
    int choice, cordX, CordY;
    int CorNum = corazzata.getN_ships(), SotNum = sottomarino.getN_ships(), FreNum = fregata.getN_ships(), LanNum = lancia.getN_ships();
    char dir;
    bool attack = false; // false = Non attaccato, true = attaccato
    
    // creazione della board vuota
    vector<vector<char>> board;
    InitializedBoard(board);

    // Stampa la board
    cout << "Battaglia Navale" << endl;
    cout << "Creazione della board" << endl;
    PrintBoard(board);

    // Lista delle navi
    cout << "Navi disponibili: " << endl;
    for(int i = 0; i < ships.size(); i++){
        cout << i+1 << ") " << ships[i]->getName() << " |Grandezza navi: "<< ships[i]->getSize()<< " |Numero navi: "<< ships[i]->getN_ships()<< endl;
    }
    do
    {
        // posizionamento delle navi
        do
        {
            cout << "Scegli che nave vuoi posizionare (1-4): ";
            cin >> choice;
        } while (choice <= 1 || choice >= 4);
        
        // switch per inserire dati negli oggetti nave
        switch (choice)
        {
        case 1: // corazzata
            if(corazzata.getN_ships() == 0){
                cout << "Corazzate finite." << endl;
            }else if (corazzata.getN_ships() != 0)
            {
                corazzata.setDirection(direction(dir)); // set H or V
                corazzata.setCord_x(cordinateX(cordX));
                corazzata.setCord_y(cordinateY(CordY));
                if(placeShips(board, corazzata.getCord_x(), corazzata.getCord_y(), corazzata.getSize(), corazzata.getDirection())){
                    cout << "Corazzata posizionata con successo!" << endl;
                    corazzata.setN_ships(CorNum - 1);
                }
            }
            break;
        case 2: // sottomarino
            sottomarino.setDirection(direction(dir));
            sottomarino.setCord_x(cordinateX(cordX));
            sottomarino.setCord_y(cordinateY(CordY));
            if(placeShips(board, sottomarino.getCord_x(), sottomarino.getCord_y(), sottomarino.getSize(), sottomarino.getDirection())){
                cout << "Sottomarino posizionato con successo!"<<endl;
                sottomarino.setN_ships(SotNum - 1);
            }
            break;
        case 3: // freagata
            fregata.setDirection(direction(dir));
            fregata.setCord_x(cordinateX(cordX));
            fregata.setCord_y(cordinateY(CordY));
            if(placeShips(board, fregata.getCord_x(), fregata.getCord_y(), fregata.getSize(), fregata.getDirection())){
                cout << "Fregata posizionato con successo!"<<endl;
                fregata.setN_ships(FreNum - 1);
            }
            break;
        case 4: // lancia
            lancia.setDirection(direction(dir));
            lancia.setCord_x(cordinateX(cordX));
            lancia.setCord_y(cordinateY(CordY));
            if(placeShips(board, lancia.getCord_x(), lancia.getCord_y(), lancia.getSize(), lancia.getDirection())){
                cout << "Lancia posizionato con successo!"<<endl;
                lancia.setN_ships(LanNum - 1);
            }
            break;
        default:
            cout << "[ERROR]: errore nello switch del posizionamento navi." << endl;
            break;
        }
        // print della board
        PrintBoard(board);
    } while (corazzata.getN_ships() != 0 && sottomarino.getN_ships() != 0 && fregata.getN_ships() != 0 && lancia.getN_ships() != 0);
    //
    cout << "Inizio del gioco...." << endl;
    do
    {
        do
        {
            cordinateX(cordX);
            cordinateY(CordY);
        } while ((cordX < 0 || cordX >= gridsize) || (CordY < 0 || CordY >= gridsize));
        cout << "Attacco a (" << cordX << "," << CordY << "): " << (IsHit(board, cordX, CordY) ? "Bersaglio colpito" : "Bersaglio mancato") << endl;
        cout << "Mappa aggiornata dopo attacco." << endl;
        PrintBoard(board);
        attack = true;
    } while (!attack);
    // verifica della nave se affondata
    
    return 0;
}
/*
1. Aggiungi parametro dove la size = punti vita per la gestione della distruzione della nave
*/