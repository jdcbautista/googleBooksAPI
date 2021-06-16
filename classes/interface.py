import csv
# from classes.query import Query
from classes.list import List
from classes.query import Query
# import 'json'
#import classes here:  books
# book_list = List(default)
# query_list = Query()

class Interface:
    def __init__(self):
        # self.query = Query(str)
        self.list = List()
        self.query = Query()
        self.resultsList = []
        self.resultsMessage = ''

    def start_app(self):
        print ("Welcome to books")

    # Options include:  Search, View List, Edit List
    # def display_options(self):
    #     pass

    def run(self):
        while True:
            mode = input("\nWelcome to Books. \nOptions:\n1. View your current book collection\n2. Look up new books\n3. Add book from latest search results to collection\n")

            # Option 1 returns a list of books
            if mode == "1":
                self.list.list_books()
            #Option 2 sends out a query
            elif mode == "2":
                query = input('Search by title:\n')
                results = self.query.send_query(query)
                print(results[0])
                self.resultsList = results[1]
                self.resultsMessage = results[0]
            #Option 3 
            elif mode == "3":
                if len(self.resultsList) > 0 and self.resultsList[0] != {} and self.resultsList[0] != "No results available":
                    # print(self.resultsMessage)
                    print(self.resultsMessage)
                    id = input('Choose a book from this list to add to your collection.\n')
                    book = self.resultsList[int(id) - 1]
                    self.list.add_book(book)
                    
                else: print("\nYour search queue is empty!")
            else: break