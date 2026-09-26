import models
from bookstore.models import read_current_user


book_dict={}
user_dict={}
library=models.BookStore(book_dict,user_dict,"0")
library.current_user=read_current_user()
library.load_books()
user_dict=library.load_users()
library.save_books()
library.save_users()
while True:
    library.save_books()
    library.save_users()
    if library.current_user=="0":
        choice = int(input("""===== 网上书店系统 =====
1. 登录
2. 注册
3. 浏览所有书籍
4. 搜索书籍
0. 退出
请选择："""))
        if choice == 1:
            library.login()
        elif choice==2:
            library.register()
            library.save_users()
        elif choice==3:
            library.show_all_books()
        elif choice==4:
            library.search_books()
        elif choice==0:
            break
        else:
            print("输入错误!")
    elif library.current_user=="admin":
        choice = int(input("""===== 管理员面板 =====
1. 浏览所有书籍
2. 搜索书籍
3. 添加新书
4. 删除书籍
5. 查看所有用户
6. 退出登录
0. 退出系统
请选择："""))
        if choice == 1:
            library.show_all_books()
        elif choice==2:
            library.search_books()
        elif choice==3:
            library.add_book()
        elif choice==4:
            book=library.search_books()
            library.delete_book(book)
            library.save_books()
        elif choice==5:
            library.show_all_users()
        elif choice==6:
            library.logout()
        elif choice==0:
            break
        else:
            print("输入错误!")
    else:
        choice = int(input(f"""===== 网上书店系统 =====
欢迎，{library.current_user}！
1. 浏览所有书籍
2. 搜索书籍
3. 借书
4. 还书
5. 查看我的借阅记录
6. 退出登录
0. 退出系统
请选择："""))
        if choice == 1:
            library.show_all_books()
        elif choice==2:
            library.search_books()
        elif choice==3:
            book=library.search_books()
            user_dict[library.current_user].borrow_book(book)
            library.save_books()
        elif choice==4:
            user_dict[library.current_user].show_borrowed()
            book=input("希望还哪一本")
            if book in user_dict[library.current_user].borrow_books:
                user_dict[library.current_user].return_book(book)
            else:
                print("未查询到该书")
            library.save_books()
        elif choice==5:
            user_dict[library.current_user].show_borrowed()
        elif choice==6:
            library.logout()
            pass
        elif choice==0:
            break
        else:
            print("输入错误!")


# 在 main.py 最后加上
input("按回车键退出...")