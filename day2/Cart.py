
product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Watch',10600),
    ('Coffee',31.22),
    ('python book2',120),
]
shopping_list = []
salary = input("Input your salary: ")
if salary.isdigit() :
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            #print(product_list.index(item),item)
            print(index,item)
        user_choice = input("选择商品 ：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:#买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    #修改输出数字的颜色红色31，绿色32 固定写法\033[32;1m%s\033[0m   其中%s 为修改颜色的数字
                    print("Add %s into shopping cart,your current salary is \033[31;1m%s\033[0m"%(p_item,salary))
                else:
                    print("\033[32;1m你的余额不足，余额为[%s]\033[0m"%salary)
            else:
                print("product code [%s] is not exist!"%user_choice)
        elif user_choice == 'q':
            print("EXIT----")
            print("------------shopping list---------")
            for p in shopping_list:
                print(p)
            print("You current balance is :",salary)
            exit()
        else:
            print("Invalid option")

