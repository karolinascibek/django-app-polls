# django-app-polls

## Wymagania:
- python 3.6.7
- xampp lub uwamp
- MySQL

## instalacja
Otwórz w folderze głównym projektu terminal 
### Środowisko virtualne
> python -m venv venv
### Aktywowanie środowiska
> venv\Scripts\activate
### Zainstaluj potrzebne paczki
> python -m pip install -r requirements.txt

# Uruchamianie
Ustaw parametry na swoją baze danych w pliku `mysite/settings` w zmiennej DATABASE

Zrób migracje danych
> python manage.py makemigrations

> python manage.py migrate

Uruchom serwer
> python manage.py runserver

W przeglądarce 
> http://127.0.0.1:8000/


