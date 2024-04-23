class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return f"Author: {self.name}"


class Book:
    total_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.author.books.append(self)
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author={self.author})"

    def __str__(self):
        return f"Book: {self.name} ({self.year}) by {self.author.name}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={self.books})"

    def __str__(self):
        return f"Library: {self.name}"


# Example usage:
if __name__ == "__main__":
    # Create authors
    author1 = Author("John Doe", "USA", "1990-01-01")
    author2 = Author("Jane Smith", "UK", "1985-05-15")

    # Create library
    library = Library("My Library")

    # Add books to the library
    book1 = library.new_book("Book 1", 2000, author1)
    book2 = library.new_book("Book 2", 2005, author2)
    book3 = library.new_book("Book 3", 2010, author1)

    # Group books by author
    print(library.group_by_author(author1))

    # Group books by year
    print(library.group_by_year(2005))
