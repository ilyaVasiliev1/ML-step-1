class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def add_page(self, count):
        self.pages += count

    def change_author(self, new_author):
        self.author = new_author

    def change_title(self, new_title):
        self.title = new_title

    def show_info(self):
        print(self.title, self.author, self.pages)

b = Book("Name", "Author", 100)
b.show_info()
b.add_page(20)
b.change_author("Potter")
b.change_title("Strange")
b.show_info()