-- DROP TABLE
DROP TABLE if EXISTS TableReservation;
DROP TABLE if EXISTS RoomReservation;
DROP TABLE if EXISTS RestaurantTable;
DROP TABLE if EXISTS HotelRooms;
DROP TABLE if EXISTS Events;
DROP TABLE if EXISTS User;
DROP TABLE if EXISTS Restaurant;
DROP TABLE if EXISTS Hotel;

-- CREATE TABLE
-- 
CREATE TABLE if not EXISTS User(
ID integer primary key autoincrement,
Name text not null,
Surname text not null,
MobilePhone text not null unique,
Username text not null unique,
Email text not null unique,
Password text not null,
FiscalCode text not null,
DateBirth date not null,
CityResidence text not null,
StreetResidence text not null,
constraint chk_pwd check (length(Password) >= 8),
constraint chk_email check (Email like '%@%.%')
);
--
CREATE TABLE if not EXISTS Restaurant(
ID integer primary key autoincrement,
Name text not null,
City text not null,
Street text not null,
ClosingDays text not null, -- (monday)
OpeningDays text not null, -- (tuesday, wednesday, thursday, friday, saturday, sunday)
ClosingTime time not null,
OpeningTime time not null,
Phone text not null unique,
Email text not null unique,
TotTables integer not null
);
--
CREATE TABLE if not EXISTS Hotel(
ID integer primary key autoincrement,
Name text not null,
City text not null,
Street text not null,
Phone text not null unique,
Email text not null unique,
TotRooms integer not null
);
--
CREATE TABLE if not EXISTS Events(
ID integer primary key autoincrement,
IDUser integer not null,
type text not null, -- wedding / birthday / meeting
EventDate date not null,
Location text not null, -- inside / outside
GuestsNumber integer not null, -- min 10
Notes text not null,
foreign key (IDUser) references User(ID),
constraint chk_gst_events check (GuestsNumber >= 10)
);
--
CREATE TABLE if not EXISTS HotelRooms(
ID integer primary key autoincrement,
IDHotel integer not null,
RoomNumber text not null, -- 101, 201, 301
Status text not null, -- (free / taken / maintance)
Type text not null, --(single room [1 person] / double room [2 people - king size bed] / twin room [2 people - 2 beds] / triple room [3 people] / suite)
foreign key (IDHotel) references Hotel(ID)
);
--
CREATE TABLE if not EXISTS RestaurantTable(
ID integer primary key autoincrement,
IDRestaurant integer not null,
Status text not null, -- (free / taken)
Position text not null, -- (inside / outside)
TableNumber integer not null,
foreign key (IDRestaurant) references Restaurant(ID)
);
--
CREATE TABLE if not EXISTS RoomReservation(
ID integer primary key autoincrement,
IDUser integer not null,
IDHotelRoom integer not null,
CheckInDate date not null,
CheckOutDate date not null, -- YYYY-MM-DD
PeopleNumber integer not null, -- min 1
ReservationStatus text not null, -- (confirmed / pending / cancelled)
Notes text not null,
foreign key (IDUser) references User(ID),
foreign key (IDHotelRoom) references HotelRooms(ID),
constraint chk_gst_room check (PeopleNumber >= 1),
constraint chk_dates check (CheckOutDate >= CheckInDate)
);
--
CREATE TABLE if not EXISTS TableReservation(
ID integer primary key autoincrement,
IDUser integer not null,
IDRestaurantTable integer not null,
ReservationDate date not null,
ReservationTime time not null,
PeopleNumber integer not null, -- min 1
ReservationStatus text not null, -- (confirmed / pending / cancelled)
Notes text not null,
foreign key (IDUser) references User(ID),
foreign key (IDRestaurantTable) references RestaurantTable(ID),
constraint chk_gst_table check (PeopleNumber >= 1)
);