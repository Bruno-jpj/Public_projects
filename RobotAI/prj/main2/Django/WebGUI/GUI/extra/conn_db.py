from django.db import connections, transaction
from django.db.utils import OperationalError, DatabaseError
from GUI.models import Cmd as c
#from  django.utils import timezone

from datetime import datetime

DB_NAME = 'comand_db'

def conn_db(timestamp, comandtext, xpos, ypos):
    # db-connection check
    try:
        connections[DB_NAME].ensure_connection()
        print(f"Connection to the DB, Established")
    except OperationalError as oe: #OperationalError -> unable to open db file, wrong db or table erased
        print(f"Connection to DB, Failed [{oe}]")
        return False
        
    # values check
    try:
        if not isinstance(timestamp, datetime):
            print("Error: timestamp not valid")
            return False
        if not isinstance(comandtext, str) or len(comandtext) == 0:
            print("Error: comandtext not valid")
            return False
        if (isinstance(xpos, int) and isinstance(ypos, int)) or (xpos is None and ypos is None):
            print("Coordinates valid")
        else:
            print(f"xpos: {xpos}, ypos: {ypos}")
            #print(type(xpos))
            #print(type(ypos))
            print("Error: Coordinates not valid")
            return False
    except Exception as e:
        print(f"Exception catched during values check: [{e}]")
        return False    
    # db insert
    try:
        with transaction.atomic(using=DB_NAME):
            c.objects.using(DB_NAME).create(
                timestamp = timestamp,
                comandtext = comandtext,
                xpos = xpos,
                ypos = ypos
            )
        print("Comand inserted correctly")
        return True
    except DatabaseError as de:
        print(f"Error. DB Error, automatic rollback {de}")
        return False
    #
#
