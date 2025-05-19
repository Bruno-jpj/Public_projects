#include<iostream>
#include<vector>
#include<string>
using namespace std;

const int gridsize = 10;
const char ship = '#', hit = 'H', miss = 'M', water = '~';

class Ship {
private:
    int size;
    int n_ships;
    int cord_x;
    int cord_y;
    int hp;
    char direction;
    string name;
public:
    Ship(int size, int n_ships, int cord_x, int cord_y, char direction, string name)
        : size(size), n_ships(n_ships), cord_x(cord_x), cord_y(cord_y), hp(size), direction(direction), name(name) {}

    int getSize() const { return size; }
    int getN_ships() const { return n_ships; }
    int getCord_x() const { return cord_x; }
    int getCord_y() const { return cord_y; }
    int getHP() const { return hp; }
    char getDirection() const { return direction; }
    string getName() const { return name; }

    void setCord_x(int x) { cord_x = x; }
    void setCord_y(int y) { cord_y = y; }
    void setDirection(char dir) { direction = dir; }
    void takeHit() { if (hp > 0) hp--; }
    bool isDestroyed() const { return hp == 0; }
};

void InitializeBoard(vector<vector<char>>& board) {
    board.assign(gridsize, vector<char>(gridsize, water));
}

void PrintBoard(const vector<vector<char>>& board) {
    cout << "  ";
    for (int i = 0; i < gridsize; i++) cout << i << " ";
    cout << endl;
    for (int i = 0; i < gridsize; i++) {
        cout << i << " ";
        for (int j = 0; j < gridsize; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

bool PlaceShip(vector<vector<char>>& board, Ship& ship) {
    int x = ship.getCord_x(), y = ship.getCord_y(), size = ship.getSize();
    char dir = ship.getDirection();

    if (dir == 'H' && y + size > gridsize) return false;
    if (dir == 'V' && x + size > gridsize) return false;
    
    for (int i = 0; i < size; i++) {
        if (dir == 'H' && board[x][y + i] != water) return false;
        if (dir == 'V' && board[x + i][y] != water) return false;
    }
    
    for (int i = 0; i < size; i++) {
        if (dir == 'H') board[x][y + i] = ship;
        else board[x + i][y] = ship;
    }
    return true;
}

bool IsHit(vector<vector<char>>& board, int x, int y, vector<Ship*>& ships) {
    if (board[x][y] == ship) {
        board[x][y] = hit;
        for (auto& s : ships) {
            if (s->getDirection() == 'H' && s->getCord_x() == x && y >= s->getCord_y() && y < s->getCord_y() + s->getSize()) {
                s->takeHit();
                cout << s->getName() << " colpita! HP rimanenti: " << s->getHP() << endl;
                if (s->isDestroyed()) cout << s->getName() << " affondata!" << endl;
                return true;
            }
            if (s->getDirection() == 'V' && s->getCord_y() == y && x >= s->getCord_x() && x < s->getCord_x() + s->getSize()) {
                s->takeHit();
                cout << s->getName() << " colpita! HP rimanenti: " << s->getHP() << endl;
                if (s->isDestroyed()) cout << s->getName() << " affondata!" << endl;
                return true;
            }
        }
    } else {
        board[x][y] = miss;
        cout << "Colpo in acqua!" << endl;
    }
    return false;
}

bool AllShipsSunk(const vector<Ship*>& ships) {
    for (const auto& s : ships) {
        if (!s->isDestroyed()) return false;
    }
    return true;
}

int GetCoordinate(const string& prompt) {
    int coord;
    do {
        cout << prompt;
        cin >> coord;
    } while (coord < 0 || coord >= gridsize);
    return coord;
}

char GetDirection() {
    char dir;
    do {
        cout << "Inserisci direzione (H/V): ";
        cin >> dir;
    } while (dir != 'H' && dir != 'V');
    return dir;
}

int main() {
    vector<vector<char>> board;
    InitializeBoard(board);
    PrintBoard(board);
    
    Ship corazzata(4, 1, 0, 0, 'H', "Corazzata");
    Ship sottomarino(3, 3, 0, 0, 'H', "Sottomarino");
    Ship fregata(2, 3, 0, 0, 'H', "Fregata");
    Ship lancia(1, 2, 0, 0, 'H', "Lancia");
    vector<Ship*> ships = {&corazzata, &sottomarino, &fregata, &lancia};
    
    for (auto& ship : ships) {
        for (int i = 0; i < ship->getN_ships(); i++) {
            do {
                ship->setDirection(GetDirection());
                ship->setCord_x(GetCoordinate("Inserisci coordinata X: "));
                ship->setCord_y(GetCoordinate("Inserisci coordinata Y: "));
            } while (!PlaceShip(board, *ship));
        }
    }
    PrintBoard(board);
    
    cout << "Inizio del gioco..." << endl;
    while (!AllShipsSunk(ships)) {
        int x = GetCoordinate("Inserisci X per attaccare: ");
        int y = GetCoordinate("Inserisci Y per attaccare: ");
        IsHit(board, x, y, ships);
        PrintBoard(board);
    }
    cout << "Tutte le navi affondate! Fine del gioco." << endl;
    return 0;
}
