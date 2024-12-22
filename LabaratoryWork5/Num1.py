class Book:
    title = "Война и мир"
    author = "Лев Толстой"
    year = "1865"

    def get_info(self):
        print("Название книги: {}, Автор: {}, Год издания: {}".
              format(self.title, self.author, self.year))

book = Book()
book.get_info()