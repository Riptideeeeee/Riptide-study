book_dict={}
user_dict={}
class Book:
    def __init__(self,book_id,title,author,price,stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    def show(self):
        print(f"书籍编号 : {self.book_id} | "
              f"书名 : 《{self.title}》 | "
              f"作者 : {self.author} | "
              f"价格 : {self.price} | "
              f"库存 : {self.stock}")
    def borrow(self):
        print("借书成功")
        self.stock =str(int(self.stock)- 1)
    def return_book(self):
        print("还书成功")
        self.stock =str(int(self.stock)+ 1)

    def save(self):
        with open("data/books.txt","a",encoding="utf-8") as f:
            f.write(self.book_id+"|"+self.title+"|"+self.author+"|"+self.price+"|"+self.stock+"|"+"0"+"\n")
class Ebook(Book):
    def __init__(self,book_id,title,author,price,stock,file_size):
        super().__init__(book_id,title,author,price,stock)
        self.file_size = file_size

    def show(self):
        # 调用父类的 show，再额外打印文件大小
        super().show()
        print(f"{self.book_id}:《{self.title}》是电子书，文件大小：{self.file_size}MB")
    def save(self):
        with open("data/books.txt","a",encoding="utf-8") as f:
            f.write(self.book_id+"|"+self.title+"|"+self.author+"|"+self.price+"|"+self.stock+"|"+self.file_size+"\n")
class User:
    def __init__(self,username,password,borrow_books):
        self.username = username
        self.password = password
        self.borrow_books = borrow_books

    def borrow_book(self,book_id):
        book_dict[book_id].borrow()
        self.borrow_books.append(book_id)

    def return_book(self,book_id):
        book_dict[book_id].return_book()
        self.borrow_books.remove(book_id)

    def show_borrowed(self):
        print(self.borrow_books)

    def save(self):
        with open("data/users.txt","a",encoding="utf-8") as f:
            f.write(self.username+"|"+self.password+"|")
            for i in range(len(self.borrow_books)):
                if i == len(self.borrow_books)-1:
                    f.write(self.borrow_books[i])
                else:
                    f.write(self.borrow_books[i]+",")
            f.write("\n")

    def register(self,name,password,borrow_books=[]):
        self.username = name
        self.password = password
        self.borrow_books=borrow_books

    def show(self):
        print(self.username+"|"+self.password+"|",end="")
        for i in range(len(self.borrow_books)):
            if i == len(self.borrow_books) - 1:
                print(self.borrow_books[i])
            else:
                print(self.borrow_books[i] + ",",end="")
class BookStore:
    def __init__(self,books,users,current_user):
        self.books = books
        self.users = users
        self.current_user = current_user

    def load_users(self):
        """从文件读取数据，返回字典"""
        try:
            with open("data/users.txt", "r", encoding="utf-8") as f:
                read = f.readlines()
        except FileNotFoundError:
            users = ["admin|123|\nTom|12323|B002\n"]
            with open("data/users.txt", "w", encoding="utf-8") as f:
                f.writelines(users)
        with open("data/users.txt", "r+", encoding="utf-8") as f:
            a = f.readline(2)
            if a == "":
                users = ["admin|123|\nTom|12323|B002\n"]
                f.writelines(users)
        with open("data/users.txt", "r", encoding="utf-8") as f:
            read = f.readlines()
        for user in read:
            user = user.strip("\n")
            part = user.split("|")
            borrowedbook = part[2].split(",")
            user_dict[part[0]] = User(part[0], part[1], borrowedbook)
        return user_dict
    def load_books(self):
        """从文件读取数据，返回字典"""
        try:
            with open("data/books.txt", "r", encoding="utf-8") as f:
                read = f.readlines()
        except FileNotFoundError:
            books = ["B001|三体|刘慈欣|68.0|10|0\nB002|活着|余华|45.0|5|0\n"]
            with open("data/books.txt", "w", encoding="utf-8") as f:
                f.writelines(books)
        with open("data/books.txt", "r+", encoding="utf-8") as f:
            a = f.readline(2)
            if a == "":
                books = ["B001|三体|刘慈欣|68.0|10|0\nB002|活着|余华|45.0|5|0\n"]
                f.writelines(books)
        with open("data/books.txt", "r", encoding="utf-8") as f:
            read = f.readlines()
        for book in read:
            book = book.strip("\n")
            part = book.split("|")
            if part[5] == '0':
                book_dict[part[0]] = Book(part[0], part[1], part[2], part[3], part[4])
            else:
                book_dict[part[0]] = Ebook(part[0], part[1], part[2], part[3], part[4], part[5])
    def save_books(self):
        with open("data/books.txt", "w", encoding="utf-8") as f:
            f.write("")
        for book in book_dict:
            book_dict[book].save()
    def save_users(self):
        with open("data/users.txt", "w", encoding="utf-8") as f:
            f.write("")
        for user in user_dict:
            user_dict[user].save()
    def register(self):
        while True:
            name = input("请输入用户名：")
            if name in user_dict or name == "0":
                print("该用户名不合规或已被使用，请重新输入")
                break
            else:
                password = input("请输入密码：")
                user_dict[name] = User(name, password, [])
                print("注册成功！")
                print(user_dict[name])
    def login(self):
        while True:
            name = input("输入0退出登录，请输入用户名：")
            if name in user_dict:
                password = input("请输入密码：")
                if password == user_dict[name].password:
                    print("登录成功")
                    self.current_user = name
                    with open("data/current_user.txt", "w", encoding="utf-8") as f:
                        f.write(name)
                    break
                else:
                    print("密码错误")
            elif name == "0":
                break
            else:
                print("未查询到用户，请检查拼写")
    def logout(self):
        a=input("是否登出账号，取消操作输入0，确认按Enter")
        if a =="0":
            print("已取消登出账号")
            pass
        else:
            print("账号已登出")
            with open("data/current_user.txt", "w", encoding="utf-8") as f:
                f.write("0")
            self.current_user = "0"
            pass
    def add_book(self):
        book_id=input("请输入书籍id（如B001）：")
        title=input("书名为：")
        author=input("作者为：")
        price=input("价格为：")
        stock=input("库存为：")
        file_size=input("文件大小为（非电子书请填0）：")
        if file_size=="0":
            book_dict[book_id]=Book(book_id, title, author, price, stock)
        else:
            book_dict[book_id]=Ebook(book_id, title, author, price, stock,file_size)
    def delete_book(self,book):
        choice = input("确认删除吗，确认请按1，取消请按0：")
        if choice == '1':
            del book_dict[book]
            print("删除成功")
        elif choice == '0':
            print("取消成功")
        else:
            print("输入错误")
    def search_books(self):
        choice=input("希望通过书名(0)搜索还是id搜索(1)：")
        if choice == "0":
            bookname=input("请输入书名：")
            bookshelf = []
            for book in book_dict:
                bookshelf.append(book_dict[book].title)
            if bookname in bookshelf:
                for book in book_dict:
                    if book_dict[book].title == bookname:
                        book_dict[book].show()
                        return book
            else:
                print("未查询到该书籍")
        elif choice == "1":
            bookid=input("请输入书籍id（如B001）：")
            if bookid in book_dict:
                book_dict[bookid].show()
                return bookid
            else:
                print("未查询到该书籍")
    def show_all_books(self):
        #显示所有书籍
        for book in book_dict:
            book_dict[book].show()
    def show_all_users(self):
        #显示所有书籍
        for user in user_dict:
            user_dict[user].show()
def read_current_user():
    try:
        with open("data/current_user.txt", "r", encoding="utf-8") as f:
            read = f.read()
    except FileNotFoundError:
        with open("data/current_user.txt", "w", encoding="utf-8") as f:
            f.write("0")
            read = "0"
    return read
def clean():
    with open("data/books.txt", "w", encoding="utf-8") as f:
        f.write("")
    with open("data/users.txt", "w", encoding="utf-8") as f:
        f.write("")
    with open("data/current_user.txt", "w", encoding="utf-8") as f:
        f.write("0")
#clean()