# django-app-polls

## Wymagania:
- python 3.6.7
- xampp lub uwamp

## instalacja
### Środowisko virtualne
> python -m venv venv
### aktywaowanie środowiska
> venv\Scripts\activate
### zainstaluj potrzebne paczki
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


