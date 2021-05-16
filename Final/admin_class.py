import pandas as pd
import csv
import os
import hashlib
from good_class import Good
import time
from store_class import Store
import logging


logging.basicConfig(level=logging.DEBUG, filename='store_logs.log',filemode='a',format='%(levelname)s-%(asctime)s -%(message)s',datefmt='%d-%b-%y %H:%M:%S')


class Admin:
    """[class for admin of store]
    """

    def __init__(self, username, password):
        """[summary]

        Args:
            username ([str]): [description]
            password ([str]): [description]
        """
        self.username = username
        self.password = password
        self.roll = "admin"
        self.notif_list = []

    def set_store(self, store):
        """[load the whole store obj for admin]

        Args:
            store ([obj]): [description]
        """
        self.store = store

    @staticmethod
    def register():
        """[static method for admin registration]

        Returns:
            [admin obj]: [description]
        """
        security_pass = '123456'
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account["username"])
        username_ = ''
        password_ = ''
        r = input("enter security pass to continue:")
        if r != security_pass:
            print("wrong security password!  \n Fail to register")
            time.sleep(2)
            return None

        while True:
            username = input("enter your username:")
            if len(username) == 0:
                print("invalid input!")
                logging.error("invalid input error")
            elif username in lst_username:
                print("This username has already exist!")
                logging.warning("Choose a duplicate username")
            else:
                username_ = username
                break

        while True:
            password = input("enter your password:")
            if len(password) == 0:
                print("invalid password!")
                logging.error("invalid password in registration")
            else:
                password_ = password
                break

        hash_password = hashlib.sha256(password_.encode("utf8")).hexdigest()
        obj_user = Admin(username_, hash_password)

        row_account = [[obj_user.username, obj_user.password, 'admin'], ]
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)

    @staticmethod
    def login():
        """[login of admin]

        """
        file_path = "account.csv"
        username = input("enter your username:")
        password = input("enter your password:")
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
        df_account = pd.read_csv(file_path)
        u_list = df_account['username']
        p_list = df_account['password']
        r_list = df_account['roll']
        for u, p, r in zip(u_list, p_list, r_list):
            if username == u and hash_password == p and r == 'admin':
                return Admin(u, p)
        else:
            return None
    def show_bills_from_file(self):
        # try:
        file_path = 'orders.csv'
        df_account = pd.read_csv(file_path)
        u_list = df_account['username']
        orders_list = df_account['order_detail']
        d_list = df_account['date']
        for u, p, r in zip(u_list, orders_list, d_list):
            print(u,p,r)
        # except:


    def add_good_to_store(self):
        """[adding product to store by admin]

        Returns:
            [tuple]: [good obj and its number]
        """
        try:
            name = input('name of the product:')
            barcode = input('barcode of the product:')
            brand = input('brand of the product:')
            price = int(input('price of the product:'))
            number =int(input('number of the product:')) 
            if name == '' or barcode =='' or brand =='' or price<0 or number <0:
                logging.error(f"add_good_to_store -> invalid input. Admin:{self.username} , input:{name},{barcode},{brand},{price},{number}")
                raise Exception("invalid input error")

            logging.info(f"add_good_to_store -> Admin:{self.username} , input:{name},{barcode},{brand},{price},{number}")
            good = Good(name, barcode, brand, price)
            self.store.add_to_store(good, number)
            return good, number
        except:
            print("Invalid input. Cheshmato baz kon!!!")
            time.sleep(2)
            


    def notification(self):
        for i in self.store.good_dict.keys():
            if self.store.good_dict[i] == 0:
                self.notif_list.append(i)

    def admin_menu(self):
        while True:
            os.system("clear||cls")
            print(f"______________________wellcome {self.username}_____________________")
            print("______________________login page -->Admin menu_____________________")
            print('1-Show Notification')
            print('2- Unlock the accounts')
            print('3-Add product to store')
            print('4-show bills')
            print('5-sign out')
            item = input('select item : ')
            if item == '1':
                os.system("clear||cls")
                print(f"______________login page --->Admin menu--->Show notifications to {self.username}_____________________")
                self.notification()
                for n in self.notif_list:
                    print(f"the stock of the {n.name} has been finished!")
                input("press Enter to return...")

            elif item =='2':
                os.system("clear||cls")
                print(f"______________login page --->Admin menu--->Unlock the accounts_____________________")
                file_path = "account.csv"
                df_account = pd.read_csv(file_path)
                u_list = df_account['username']
                s_list = df_account['status']
                
                for i,(u,s) in enumerate(zip(u_list,s_list)):
                    if str(s) == '0':
                        print(f" {i}. {u}")
                choise = input("choose the  user name account you want to unlock: ")
                try:
                    for i,u in enumerate(u_list):
                        if choise == u:
                            df_account.at[i,'status'] = 1
                            df_account.to_csv(r'account.csv', index = False)
                            print("account status changes")
                            time.sleep(1)
                except:
                    pass

            elif item == '3':
                os.system("clear||cls")
                print(f"______________login page --->Admin menu--->Add New Products to Store_____________________")
                print("For adding a new product you need to enter its specification ")
                try:
                    g, n = self.add_good_to_store()
                    logging.info("a new product has been added to store")
                    # self.store.add_to_store(g,n)
                    input("press Enter to return...")
                except:
                    pass

            elif item =='4':
                os.system("clear||cls")
                print(f"______________login page --->Admin menu--->Show all bills of store to {self.username}_____________________")
                self.show_bills_from_file()
                input("press any keys to back to menu")

            elif item == '5':
                break
