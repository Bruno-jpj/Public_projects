// librerie
#include <iostream>
#include <vector>
#include <string>
#include <list>
using namespace std;

// func
#include "ship_func.h"

// classi
#include "ship_class.h"

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
    int choice, cordX, cordY;
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
        cout << i+1 << ") " << ships[i]->getName() 
             << " | Grandezza nave: " << ships[i]->getSize() 
             << " | Numero navi: " << ships[i]->getN_ships() << endl;
    }

    // Posizionamento navi
    do {
        do {
            cout << "Scegli che nave vuoi posizionare (1-4): ";
            cin >> choice;
        } while (choice < 1 || choice > 4);
        
        switch (choice) {
        case 1: // corazzata
            if(corazzata.getN_ships() == 0){
                cout << "Corazzate finite." << endl;
            } else {
                corazzata.setDirection(direction(dir)); 
                corazzata.setCord_x(cordinateX(cordX));
                corazzata.setCord_y(cordinateY(cordY));

                if(placeShips(board, corazzata.getCord_x(), corazzata.getCord_y(), corazzata.getSize(), corazzata.getDirection())){
                    cout << "Corazzata posizionata con successo!" << endl;
                    corazzata.setN_ships(corazzata.getN_ships() - 1);
                }
            }
            break;

        case 2: // sottomarino
            if(sottomarino.getN_ships() == 0){
                cout << "Sottomarini finiti." << endl;
            } else {
                sottomarino.setDirection(direction(dir));
                sottomarino.setCord_x(cordinateX(cordX));
                sottomarino.setCord_y(cordinateY(cordY));

                if(placeShips(board, sottomarino.getCord_x(), sottomarino.getCord_y(), sottomarino.getSize(), sottomarino.getDirection())){
                    cout << "Sottomarino posizionato con successo!"<<endl;
                    sottomarino.setN_ships(sottomarino.getN_ships() - 1);
                }
            }
            break;

        case 3: // fregata
            if(fregata.getN_ships() == 0){
                cout << "Fregate finite." << endl;
            } else {
                fregata.setDirection(direction(dir));
                fregata.setCord_x(cordinateX(cordX));
                fregata.setCord_y(cordinateY(cordY));

                if(placeShips(board, fregata.getCord_x(), fregata.getCord_y(), fregata.getSize(), fregata.getDirection())){
                    cout << "Fregata posizionata con successo!"<<endl;
                    fregata.setN_ships(fregata.getN_ships() - 1);
                }
            }
            break;

        case 4: // lancia
            if(lancia.getN_ships() == 0){
                cout << "Lance finite." << endl;
            } else {
                lancia.setDirection(direction(dir));
                lancia.setCord_x(cordinateX(cordX));
                lancia.setCord_y(cordinateY(cordY));

                if(placeShips(board, lancia.getCord_x(), lancia.getCord_y(), lancia.getSize(), lancia.getDirection())){
                    cout << "Lancia posizionata con successo!"<<endl;
                    lancia.setN_ships(lancia.getN_ships() - 1);
                }
            }
            break;

        default:
            cout << "[ERROR]: errore nello switch del posizionamento navi." << endl;
            break;
        }

        // print della board
        PrintBoard(board);

    } while (corazzata.getN_ships() != 0 || sottomarino.getN_ships() != 0 || fregata.getN_ships() != 0 || lancia.getN_ships() != 0);

    cout << "Inizio del gioco...." << endl;
    
    // Attacchi
    do {
        do {
            // chiedi coordinate X e Y
            cordX = cordinateX(cordX);
            cordY = cordinateY(cordY);

        } while ((cordX < 0 || cordX >= gridsize) || (cordY < 0 || cordY >= gridsize));

        cout << "Attacco a (" << cordX << "," << cordY << "): " 
             << (IsHit(board, cordX, cordY) ? "Bersaglio colpito" : "Bersaglio mancato") << endl;

        cout << "Mappa aggiornata dopo attacco:" << endl;
        PrintBoard(board);

        attack = true;

        // verifica delle navi se affondate
        if(IsSunk(board, corazzata.getCord_x(), corazzata.getCord_y(), corazzata.getSize(), corazzata.getDirection())){
            cout << "Corazzata affondata!" << endl;
        }
        if(IsSunk(board, sottomarino.getCord_x(), sottomarino.getCord_y(), sottomarino.getSize(), sottomarino.getDirection())){
            cout << "Sottomarino affondato!" << endl;
        }
        if(IsSunk(board, fregata.getCord_x(), fregata.getCord_y(), fregata.getSize(), fregata.getDirection())){
            cout << "Fregata affondata!" << endl;
        }
        if(IsSunk(board, lancia.getCord_x(), lancia.getCord_y(), lancia.getSize(), lancia.getDirection())){
            cout << "Lancia affondata!" << endl;
        }

        // check se tutte le navi sono affondate
        if(allShipsSunk(board)){
            cout << "Tutte le navi sono affondate! Hai vinto!" << endl;
            break;
        }

    } while(true);

    return 0;
}