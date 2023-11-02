from project.user import User

class Library:
    def __init__(self):
        self.user_records = []    # list of User's objects
        self.books_available = {}  # authors: [books]
        self.rented_books = {}    # username: {book_name: days_left}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):

        if author in self.books_available:
            collection = self.books_available[author]  # list of books
            if book_name in collection:
                self.books_available[author].remove(book_name)
                if user.username not in self.rented_books:
                    self.rented_books[user.username] = {}
                self.rented_books[user.username].update({book_name: days_to_return})
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

            else:
                for v in self.rented_books.values():
                    if book_name in v:
                        days = v[book_name]
                        # "The book "{book_name}" is already rented and will be available in {days_to_return provided by the user rented the book} days!"
                        return f'The book "{book_name}" is already rented and will be available in {days} days!'


    def return_book(self, author: str, book_name: str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        self.rented_books[user.username].pop(book_name)
        self.books_available[author].append(book_name)
        user.books.remove(book_name)
        return
