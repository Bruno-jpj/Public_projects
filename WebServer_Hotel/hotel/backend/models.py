# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Events(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('User', on_delete=models.CASCADE, db_column='IDUser')  # Field name made lowercase.
    type = models.TextField()
    eventdate = models.DateField(db_column='EventDate')  # Field name made lowercase.
    location = models.TextField(db_column='Location')  # Field name made lowercase.
    guestsnumber = models.IntegerField(db_column='GuestsNumber')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Events'


class Hotel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    city = models.TextField(db_column='City')  # Field name made lowercase.
    street = models.TextField(db_column='Street')  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', unique=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', unique=True)  # Field name made lowercase.
    totrooms = models.IntegerField(db_column='TotRooms')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hotel'


class Hotelrooms(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idhotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, db_column='IDHotel')  # Field name made lowercase.
    roomnumber = models.TextField(db_column='RoomNumber')  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase.
    type = models.TextField(db_column='Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HotelRooms'


class Restaurant(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    city = models.TextField(db_column='City')  # Field name made lowercase.
    street = models.TextField(db_column='Street')  # Field name made lowercase.
    closingdays = models.TextField(db_column='ClosingDays')  # Field name made lowercase.
    openingdays = models.TextField(db_column='OpeningDays')  # Field name made lowercase.
    closingtime = models.TimeField(db_column='ClosingTime')  # Field name made lowercase.
    openingtime = models.TimeField(db_column='OpeningTime')  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', unique=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', unique=True)  # Field name made lowercase.
    tottables = models.IntegerField(db_column='TotTables')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Restaurant'


class Restauranttable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idrestaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, db_column='IDRestaurant')  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase.
    position = models.TextField(db_column='Position')  # Field name made lowercase.
    tablenumber = models.IntegerField(db_column='TableNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RestaurantTable'


class Roomreservation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('User', on_delete=models.CASCADE, db_column='IDUser')  # Field name made lowercase.
    idhotelroom = models.ForeignKey(Hotelrooms, on_delete=models.CASCADE, db_column='IDHotelRoom')  # Field name made lowercase.
    checkindate = models.DateField(db_column='CheckInDate')  # Field name made lowercase.
    checkoutdate = models.DateField(db_column='CheckOutDate')  # Field name made lowercase.
    peoplenumber = models.IntegerField(db_column='PeopleNumber')  # Field name made lowercase.
    reservationstatus = models.TextField(db_column='ReservationStatus')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoomReservation'


class Tablereservation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('User', on_delete=models.CASCADE, db_column='IDUser')  # Field name made lowercase.
    idrestauranttable = models.ForeignKey(Restauranttable, on_delete=models.CASCADE, db_column='IDRestaurantTable')  # Field name made lowercase.
    reservationdate = models.DateField(db_column='ReservationDate')  # Field name made lowercase.
    reservationtime = models.TimeField(db_column='ReservationTime')  # Field name made lowercase.
    peoplenumber = models.IntegerField(db_column='PeopleNumber')  # Field name made lowercase.
    reservationstatus = models.TextField(db_column='ReservationStatus')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TableReservation'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    surname = models.TextField(db_column='Surname')  # Field name made lowercase.
    mobilephone = models.TextField(db_column='MobilePhone', unique=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username', unique=True)
    email = models.TextField(db_column='Email', unique=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    fiscalcode = models.TextField(db_column='FiscalCode')  # Field name made lowercase.
    datebirth = models.DateField(db_column='DateBirth')  # Field name made lowercase.
    cityresidence = models.TextField(db_column='CityResidence')  # Field name made lowercase.
    streetresidence = models.TextField(db_column='StreetResidence')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
