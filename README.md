# README zadania 9_4

W folderze app jest aplikacja, a w folderze api jest api.

Należy zainstalować requirements.txt


Format w którym podaje sie dane w PUT lub POST:
``` python

{
        "opinion": "Wspaniały film, uwielbiam",
        "title": "Milczenie Owiec",
        "watched": true
    }

```
Naley zadbać o to żeby w headers było zawarte:
```
headers: {
    'Content-Type': 'application/json',
  }
```
Obsługa API

GET http://127.0.0.1:5000/api/v1/movies/ - zwraca wszystkie filmy w formacie JSON

GET http://localhost:5000/api/v1/movies/{movie_id}/ - zwraca pojedyńczy film w formacie JSON

POST http://localhost:5000/api/library/albums/ - dodaje nowy film - zapytanie wymaga danych w formacie JSON

DELETE http://localhost:5000/api/v1/movies/{movie_id} - usuwa pojedyńczy film w formacie JSON

PUT http://localhost:5000/api/v1/movies/{movie_id} - aktualziuje film na podstawie podanego id - zapytanie wymaga danych w formacie JSON

