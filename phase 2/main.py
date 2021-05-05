from user_class import User
from store_class import Store
from good_class import Good
from admin_class import Admin
import time
import os


my_store = Store()
my_store.load_repository()

while True:
    os.system("clear||cls")
    print("_________________________Wellcome to fgh store__________________________")
    print("________________________________________________________________________")
    print("1-login")
    print("2-register")
    answer=input("what do you want to do: ")
    if answer =='1':
        roll = input("1.user\n2.admin\nselect your roll: ")
        if roll =='1':
            user_obj = User.login()
            
            if user_obj ==None:
                print("You do not have an account")
                time.sleep(1.5)
                continue
            else:
                user_obj.set_store(my_store)
                user_obj.user_menu()
               
        elif roll =='2':
            admin_obj = Admin.login()

            if admin_obj ==None:
                print("You do not have an account")
                time.sleep(1.5)
                continue
            else:
                admin_obj.set_store(my_store)
                admin_obj.admin_menu()
                
        else:
            continue
    elif answer =='2':
        roll = input("1.user\n2.admin\nselect your roll: ")
        if roll =='1':
            User.register()
        elif roll =='2':
            admin_ = Admin.register()

        else:
            continue
    else:
        continue

