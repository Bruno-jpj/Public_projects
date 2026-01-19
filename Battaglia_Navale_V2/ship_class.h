#include <iostream>
#include <string>

using namespace std;

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