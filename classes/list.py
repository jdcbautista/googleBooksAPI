import os
import csv
from classes.book import Book

class List:
    def __init__(self):
        self.books_list = Book.objects()
        # self.list_name = list_name

    def list_books(self):
        print('\n')
        if len(self.books_list) > 0:
            for i, book in enumerate(self.books_list):
                # print(f'{i + 1}. {book.title} {book.author} {book.publisher}')
                print("%(title)s by %(authors)s published by %(publisher)s" % { "title": book.title, "authors": book.authors,"publisher": book.publisher})
        else: print("Your collection is empty.")

    def add_book(self,book):
        print('\n')
        self.books_list.append(Book(**book))
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/books.csv")

        with open(path, 'w') as csvfile:
            book_to_csv = csv.writer(csvfile, delimiter=',')
            book_to_csv.writerow(['title','authors','publisher'])
            for book in self.books_list:
                book_to_csv.writerow([book.title, book.authors, book.publisher])