class Books:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} {self.author} {self.year}"


lst2 = [
    Books(title='Harry Potter and the Philosopher\'s Stone', author='J.K. Rowling', year=1997),
    Books(title='To Kill a Mockingbird', author='Harper Lee', year=1960),
    Books(title='The Great Gatsby', author='F. Scott Fitzgerald', year=1925)
]
