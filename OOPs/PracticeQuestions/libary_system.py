class Libarary:
    def __init__(self):
        self.books={}

    def add_books(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
            print(f"One more added {book_name} added. ")
            print("Book already exists.")
        else:
            self.books[book_name]=1
            print(f"{book_name} Book added successfully.")

    def issue_books(self, book_name):
        if book_name in self.books:
            if self.books[book_name]>0:
                self.books[book_name] -=1
                print(f"Book '{book_name}' issued successfully.")
            else:
                print(f"Book '{book_name}' is currently unavailable.")
        else:
            print(f"Book '{book_name}' does not exist in the library.")

    def return_books(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
            print(f"Book '{book_name}' returned successfully.")
        else:
            print(f"Book '{book_name}' does not exist in the library.")

    def total_books(self):
        total = sum(self.books.values())
        print(f"Total books in the library: {total}")

library= Libarary()
library.add_books("Python Programming")
library.add_books("Java Programming")
library.issue_books("Python Programming")
library.return_books("Python Programming")
library.add_books("Python Programming")
library.total_books()

