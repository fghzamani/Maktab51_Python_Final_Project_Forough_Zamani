from user_class import User
from store_class import Store
from good_class import Good
import logging
import time
import os
from admin_class import Admin

logging.basicConfig(level=logging.DEBUG,filename='store_logs.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
my_store = Store()
my_store.load_repository()
counter1 = 0
counter2 = 0  # counter for counting wrong info login of an existing account 

# try:
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
            if user_obj =='False':
                pass
            elif user_obj ==None:
                print("You do not have an account")
                counter1 = counter1 +1
                time.sleep(1.5)

            else:
                
                
                user_obj.set_store(my_store)
                user_obj.user_menu()

            if counter1 ==3:
                print("your login info was not founded. ")
                print("\n seems you do not have account. You can make one by registering")
                time.sleep(4)
                break

        elif roll =='2':
            admin_obj = Admin.login()

            if admin_obj ==None:
                print("You do not have an account")
                counter1 = counter1 +1
                time.sleep(1.5)
                continue
            else:
                logging.info('Admin has been login to system.')
                admin_obj.set_store(my_store)
                admin_obj.admin_menu()
                logging.info('Admin has been login to system.')
            
            if counter1 ==3:
                print("your login info was not founded. ")
                print("\n seems you do not have account. You can make one by registering")
                time.sleep(4)
            
                input("press any keys to exit")
                break
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
# except:
#     print("invalid input! try again!")
#     input("press any keys to repeat")
#     time.sleep(4)
