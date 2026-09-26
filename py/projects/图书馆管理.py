class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def show(self):
        print(f"书名 : {self.title}\n作者 : {self.author}\n是否被借 : {self.is_borrowed}")

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print("借书成功")
        else:
            print("已被借走")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("还书成功")
        else:
            print("未被借走")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def show_all(self):
        for book in self.books:
            book.show()

    def borrow_book(self,title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                break
            else:
                print("没找到")

    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                break
            else:
                print("没找到")
    def find_book(self,title):
        for book in self.books:
            if book.title == title:
                book.show()
                break
            else:
                print("没找到")

# 创建图书馆
library = Library()

# 创建书
book1 = Book("三体", "刘慈欣")
book2 = Book("活着", "余华")
book3 = Book("百年孤独", "马尔克斯")

# 添加到图书馆
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# 显示所有书
library.show_all()

# 借书
library.borrow_book("三体")
print("借了本三体")
library.borrow_book("三体")  # 再借一次，提示已被借走
print("又借了本三体")
# 显示状态
library.show_all()

# 还书
library.return_book("三体")

# 最终状态
library.show_all()