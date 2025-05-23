# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Biglietto(models.Model):
    utente = models.ForeignKey('Utente', models.DO_NOTHING)
    treno = models.ForeignKey('Treno', models.DO_NOTHING)
    tratta = models.ForeignKey('Tratta', models.DO_NOTHING)
    nominativo = models.TextField(blank=True, null=True)
    data_acquisto = models.TextField()
    data_viaggio = models.TextField()
    prezzo = models.FloatField()
    tipo_biglietto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Biglietto'


class Metodopagamento(models.Model):
    utente = models.ForeignKey('Utente', models.DO_NOTHING)
    tipo = models.TextField()
    numero_carta = models.TextField(blank=True, null=True)
    scadenza = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MetodoPagamento'


class Stazione(models.Model):
    nome = models.TextField()
    citta = models.TextField()

    class Meta:
        managed = False
        db_table = 'Stazione'


class Tratta(models.Model):
    stazione_partenza = models.ForeignKey(Stazione, models.DO_NOTHING)
    stazione_arrivo = models.ForeignKey(Stazione, models.DO_NOTHING, related_name='tratta_stazione_arrivo_set')
    durata = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tratta'


class Treno(models.Model):
    nome = models.TextField()
    tipo = models.TextField()
    richiede_nominativo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Treno'


class Trenostazione(models.Model):
    treno = models.ForeignKey(Treno, models.DO_NOTHING)
    stazione = models.ForeignKey(Stazione, models.DO_NOTHING)
    orario_arrivo = models.TextField(blank=True, null=True)
    orario_partenza = models.TextField(blank=True, null=True)
    ordine_di_passaggio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrenoStazione'


class Utente(models.Model):
    nome = models.TextField()
    cognome = models.TextField()
    codicefiscale = models.TextField()
    email = models.TextField(unique=True)
    username = models.TextField()
    pwd = models.TextField()

    class Meta:
        managed = False
        db_table = 'Utente'
