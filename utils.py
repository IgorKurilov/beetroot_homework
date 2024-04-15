# writen by Igor Kurilov
import datetime
import random
import logging
import csv
import json

# додамо логування
logging.basicConfig(filename='book.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Початкові дані про книги
BOOKS = [
    {
        "name": "Dune",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 896,
        "entry_added": datetime.datetime(2023, 11, 15, 12, 13, 14),
    },
    {
        "name": "Dune Messiah",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 256,
        "entry_added": datetime.datetime(2023, 12, 16, 20, 0, 11),
    },
    {
        "name": "Murder on the Orient Express",
        "author": " Agatha Christie",
        "genre": "Crime novel",
        "pages": 256,
        "entry_added": datetime.datetime(2021, 10, 30, 7, 43, 28),
    },
]

def view_books():
    logging.info('User selected to view all books')
    print("\nBooks:")
    for book in BOOKS:
        print(f"'{book['name']}' by {book['author']} is {book['genre']} and has {book['pages']} pages")
        print("=" * 60)

def add_book():
    logging.info('User selected to add a new book')
    print("\nAdding a new book:")
    name = input("Введіть назву книги: ")
    logging.info(f'User entered name: {name}')
    author = input("Введіть автора книги: ")
    logging.info(f'User entered author: {author}')
    genre = input("Введіть жанр книги: ")
    logging.info(f'User entered genre: {genre}')

    # Введення кількості сторінок
    while True:
        pages_input = input("Введвть кількість сторінок (опціонально): ")
        logging.info(f'User entered pages: {pages_input}')
        if not pages_input:
            pages = None  # Якщо користувач не ввів нічого, то None
            break
        try:
            pages = int(pages_input)  # Спробуємо перевести введене значення у ціле число
            break
        except ValueError:
            print("Введіть коректне значення кількості сторінок.")
            logging.error('Invalid input for pages')

    entry_added = datetime.datetime.now()

    # Додавання нової книги до списку
    BOOKS.append({
        "name": name,
        "author": author,
        "genre": genre,
        "pages": pages,
        "entry_added": entry_added,
    })
    logging.info('New book added successfully')
    save_books_to_csv_and_json()  # Збережемо книги у файл

def random_book():
    logging.info('User selected to view a random book')
    random_book = random.choice(BOOKS)
    print("Randomly selected book:")
    print(f"'{random_book['name']}' by {random_book['author']} is {random_book['genre']} and has {random_book['pages']} pages")
    print("=" * 60)

def save_books_to_csv_and_json():
    logging.info('Saving books to CSV and JSON files')
    # Збережемо книги у CSV
    with open('books.csv', 'w', newline='', encoding='utf-8') as csv_file:    
        fieldnames = ["name", "author", "genre", "pages", "entry_added"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(BOOKS)

    # Збережемо книги у JSON
    json_books = []
    for book in BOOKS:
        # перетворення `datetime` атрибутів `entry_added` у POSIX timestamp
        book['entry_added'] = book['entry_added'].timestamp()
        json_books.append(book)

    with open('books.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_books, json_file, ensure_ascii=False, indent=4)
