# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bigliettoabbonamento(models.Model):
    data_acquisto = models.DateTimeField()
    data_inizio = models.DateTimeField()
    data_fine = models.DateTimeField()
    prezzo = models.FloatField()
    classe_vagone = models.TextField()
    numero_persone = models.IntegerField()
    utente = models.ForeignKey('Utente', on_delete=models.CASCADE)
    treno = models.ForeignKey('Treno', on_delete=models.PROTECT)
    tratta = models.ForeignKey('Tratta', on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'BigliettoAbbonamento'


class Metodopagamento(models.Model):
    tipo = models.TextField()
    numero_carta = models.IntegerField()
    cvv = models.IntegerField()
    data_scadenza = models.DateField(blank=True, null=True)
    utente = models.ForeignKey('Utente', on_delete=models.CASCADE)

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
    durata = models.TimeField()
    stazione_arrivo = models.ForeignKey(Stazione, on_delete=models.PROTECT, db_column='stazione_arrivo')
    stazione_partenza = models.ForeignKey(Stazione, on_delete=models.PROTECT, db_column='stazione_partenza', related_name='tratta_stazione_partenza_set')

    class Meta:
        managed = False
        db_table = 'Tratta'


class Treno(models.Model):
    nome = models.TextField()
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'Treno'


class Trenostazione(models.Model):
    orario_arrivo = models.DateTimeField()
    orario_partenza = models.DateTimeField()
    treno = models.ForeignKey(Treno, on_delete=models.CASCADE)
    stazione = models.ForeignKey(Stazione, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'TrenoStazione'


class Utente(models.Model):
    nome = models.TextField()
    cognome = models.TextField()
    codicefiscale = models.TextField()
    username = models.TextField()
    email = models.TextField(unique=True)
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'Utente'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
