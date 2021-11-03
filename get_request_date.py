import requests

URL_BOOKS='http://127.0.0.1:8000/lib/api/books/all'
data_books=requests.get(URL_BOOKS).json()
print(data_books)
for el in data_books:
    print(el)