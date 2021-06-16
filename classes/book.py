import csv
import os.path

class Book:
    
    def __init__(self, title, authors, publisher):
        self.title = title
        self.authors = authors
        self.publisher = publisher

    # Generates book list from csv file
    @classmethod
    def objects(cls):
        books_list = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path,"../data/books.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(dict(row))
                books_list.append(Book(**dict(row)))

            return books_list