class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def get_info(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nГод издания: {self.year}\nКоличество страниц: {self.pages}"

    def change_page_count(self, new_count):
        self.pages = new_count

    def __str__(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nГод издания: {self.year}\nКоличество страниц: {self.pages}"


book1 = Book("Война и мир", "Толстой", 1869, 1225)
book2 = Book("Преступление и наказание", "Достоевский", 1866, 671)
print(book1.get_info())
print(book2.get_info())

book1.change_page_count(1337)

print(book1)