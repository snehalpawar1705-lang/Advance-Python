class Library:
    def __init__(self):
        print = input("Enter the title:")
        print = input("Enter the author:")

    def add(self):
        #creating a list of books
        book_name = ["The Hobbit","Pride and Prejudice"]
        print("Book in library:")

        #add the elememt in the list
        book_name.append("The Odessey")
        print("The new list is:",book_name)

    def display(self):
        print("book_name:",self.book_name)