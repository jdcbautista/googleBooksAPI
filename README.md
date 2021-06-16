# Google Books API Command Line Interface


## Overview
This command line interface allows the user to:
1. Type in a search query and retreive a list of five results
2. View a book's title, author, and publishing company
3. Select and save a book from their search results to a personal reading list
4. View their own reading list

Since it was requested that no additional features be implemented, I refrained from implementing the ability to delete entries from the reading list.  Entries can be deleted manually from the books.csv file located under data, for testing purposes.


## Instructions

1. Activate Virtual Environment
    source venv/bin/activate

2. Run start.py
    python start.py

3. CLI:  The command line interface has three options and should notify the user after each time the user is prompted for an input.


## Initial Thoughts

I began by prototyping my approach with both software architecture diagramming and pseudocode.  This led to me to deciding to divide my components into the following:

1. Interface: Requests and handles user prompts
2. Query Handler:  Handles the Google Books API call, and the parsing of the json format response.
3. List Handler:  Handles a user's reading list locally, but can also be easily refactored to communicate with a server-side database.
4. Book Class Component:  Helper component to List Handler.  It sets up an object structure for books, and generates a list from the database.

From there, I wrote out a series of user stories.

1. The user can interact with a command line interface
2. From the CLI, a user can query a search.
3. From the CLI, a user can select a book from their search results to add to their reading list.
4. From the CLI, a user can view their current reading list.


## Final Thoughts
I missed the opportunity to provide an idea of my process and approach through version control history, as I worked locally and created my git repo only after I meeting all the project criteria.  I also failed to demonstrate any testing, but I intend to remedy that after your team's initial feedback. 