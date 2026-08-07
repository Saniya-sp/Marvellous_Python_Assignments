"""WAP to implement a class named BookStore with the following specifications
The class should contain two instance variables:
    -Name(book name)
    -Author(book author)
The class should contain one class variable
    -NoOfBooks(initialize to zero)
Define a constructor (__init__) that accepts Name and Author and initializes instance variables
Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created
Implement an instance method:
    -Display()- should display book details in format:
    <BookName> by <Author>. No of books <NoOfBooks>.
"""

class BookStore:
    NoOfBooks = 0

    def __init__(self, Name, Author):

        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1
        self.BookCount = BookStore.NoOfBooks   # Store count for this object

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books {self.BookCount}")
        

Obj1 = BookStore('Saniya', "Hello world")
Obj1.Display()

Obj2 = BookStore('SaniyaNew', "Hello world new")
Obj2.Display()