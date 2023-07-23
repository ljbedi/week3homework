from flask import Flask 
from controllers.books_controller import book_blueprint

app = Flask(__name__)
app.register_blueprint(book_blueprint)

# function to add a book 
# function to remove a book 
# function to show a certain book 