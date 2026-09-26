key=123
apple=0
banana=0
orange=0
grape=0
while key !=0:
    print(f"1. 苹果 - 5元 现在你有 {apple} 个苹果")
    print(f"2. 香蕉 - 3元 现在你有 {banana} 个香蕉")
    print(f"3. 橙子 - 4元 现在你有 {orange} 个橙子")
    print(f"4. 葡萄 - 8元 现在你有 {grape} 个葡萄")
    print("0. 按0结束购买")
    key=int(input("请选择商品"))
    if key==1:
        apple+=1
        print("买一个苹果")
    elif key==2:
        banana+=1
        print("买一个香蕉")
    elif key==3:
        orange+=1
        print("买一个橘子")
    elif key==4:
        grape+=1
        print("买一个葡萄")
    elif key==0:
        print("结束购买，这是清单")
    else:
        print("这个数超出范围了")
print(f"苹果:{apple}\n香蕉:{banana}\n橘子:{orange}\n葡萄:{grape}")
print("花了",apple*5+banana*3+orange*4+grape*8,"块钱")
