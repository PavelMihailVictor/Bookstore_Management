


class book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Genre:", self.genre)
        print("Price:", self.price)

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the bookstore.")
        else:
            print("Bookstore Inventory:")
            for book in self.books:
                print("-" * 30)
                book.display_info()

def main():
    bookstore = Bookstore()

    while True:
        print("\Bookstore Managment System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Exit")

        choice = input("Enter your Choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author name: ")
            genre = input("Enter the book genre: ")
            price = float(input("Enter the book price: "))
            book = Book(title, author, genre, price)
            bookstore.add_book(book)
            print("Book added successfully!")
        elif choice == "2":
            bookstore.display_books()
        elif choice == "3":
            print("Exiting Bookstore Management System...")
            break
        else:
            print("Invalid choice. Please try again.")

    if __name__ == "__main__":
        main()
