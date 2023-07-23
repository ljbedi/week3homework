from models.book import *

book1 = Book("Game of Thrones", "George RR Martin", "Fantasy", True)
book2 = Book("Japan", "Lonely Planet", "Travel Guide", True )
book3 = Book("Klara and the Sun", "Kazuo Ishiguro", "Science Fiction", False)

books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break

    books.remove(book_to_delete)



