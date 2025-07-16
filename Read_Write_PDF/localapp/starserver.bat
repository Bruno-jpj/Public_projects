@echo off

:: Vai nella directory del progetto
cd /d C:\Users\USER\Desktop\Cose\Codici\GitHub\Public_projects\Read_Write_PDF\

echo Attivazione ambiente virtuale...
call venv\Scripts\activate.bat

:: Vai nella cartella che contiene manage.py
cd localapp

echo Avvio del server Django...
python manage.py runserver

pause
