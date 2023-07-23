from models.book import Book 

book1 = Book("Game of Thrones", "George RR Martin", "Fantasy")
book2 = Book("Japan", "Lonely Planet", "Travel Guide")
book3 = Book("Klara and the Sun", "Kazuo Ishiguro", "Science Fiction")

book_list = [book1, book2, book3]

def add_new_book(book):
    book_list.append(book)

def delete_book(book_title):
    book_to_delete = None
    for book in book_list:
        if book.title == book_title:
            book_to_delete = book
            break

    book_list.remove(book_to_delete)



