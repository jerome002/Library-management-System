# Pyhon CRUD project
class Book:
    def __init__(self, book_id,title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}"
   
