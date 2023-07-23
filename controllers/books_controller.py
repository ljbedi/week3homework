from flask import Blueprint, render_template, request, redirect

from models.book import *
from models.book_list import books, add_new_book, delete_book

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def index():
    return render_template("index.jinja", title="LIBRARY", book_list=books)

@book_blueprint.route("/books", methods=['POST'])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    checked_out = False 
    new_book = Book(book_title, book_author, book_genre, checked_out)
    add_new_book(new_book)
    return redirect('/books')

@book_blueprint.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect('/books')


# Provide the following functionality:

# List all Books - DONE 
# Show an individual Book - cannot figure out - indexes??? 
# Add a new Book to the Library. - DONE
# Remove a Book from the Library - DONE (but only on bottom part - how to copy same as above??? 

# Extension - show if available or checked out 
# IF BOOK IS AVAILABLE, SHOW AS AVAILBABLE IF NOT SHOW AS UNAVAILABLE
# if checked_out == true then return/print appropiate outcome 

#  add property, checked_out as True or False, a function to print whether true or false 

