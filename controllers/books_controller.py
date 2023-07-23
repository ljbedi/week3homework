from flask import Blueprint, render_template, request, redirect
from models.book_list import book_list, add_new_book, delete_book 
from models.book import *

book_blueprint = Blueprint("book", __name__)


# INDEX is show all 

@book_blueprint.route('/books')
def index():
    return render_template("index.jinja", title = "LIBRARY", book_list=book_list)

@book_blueprint.route('/books', methods = ["POST"])
def add_book():
    book_title = request.form['title']
    book_author = request.form['author']
    book_genre = request.form['genre']
    new_book = Book(book_title, book_author, book_genre)
    add_new_book(new_book)
    return redirect('/books')

@book_blueprint.route('/books/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect('/books')


# @book_blueprint.route("/books", methods=['POST'])
# def add_book():
#     book_title = request.form['title']
#     book_author = request.form['author']
#     book_genre = request.form['genre']
#     new_book = Book(book_title, book_author, book_genre)
#     add_new_book(new_book)
#     return redirect('/books')

# @book_blueprint.route('/books/delete/<title>', methods=['POST'])
# def delete(title):
#     delete_book(title)
#     return redirect('/books')

# Provide the following functionality:

# List all Books
# Show an individual Book
# Add a new Book to the Library.
# Remove a Book from the Library