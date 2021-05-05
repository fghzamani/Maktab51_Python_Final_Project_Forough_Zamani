import pandas as pd
import csv
import os
import hashlib
#form store_class import Store
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

    def set_store(self,store):
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
        r=input("enter security pass to continue:")
        if r !=security_pass:
            print("wrong security password!  \n Fail to register")
            time.sleep(2)
            return None

        while True:
            username = input("enter your username:")
            if len(username)==0:
                print("invalid input!")
            elif username in lst_username:
                print("This username has already exist!")
            else:
                username_ = username
                break

        while True:
            password = input("enter your password:")
            if len(password)==0:
                print("invalid password!")
            else:
                password_ = password
                break

        hash_password = hashlib.sha256(password_.encode("utf8")).hexdigest()
        obj_user = Admin(username_, hash_password)
        

        row_account = [[obj_user.username, obj_user.password , 'admin'],]
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
        for u,p,r in zip(u_list,p_list,r_list):
            if username ==u and hash_password ==p and r=='admin':
                return Admin(u,p)
        else:
            return None
        
    def add_good_to_store(self):
        """[adding product to store by admin]

        Returns:
            [tuple]: [good obj and its number]
        """
        name = input('name of the product:')
        barcode= input('barcode of the product:')
        brand = input('brand of the product:')
        price = input('price of the product:')
        number = input('number of the product:')
        good = Good(name,barcode,brand,price)
        self.store.add_to_store(good,number)
        return good,number

    def notification(self):
        """[adding notifications into a lis]
        """
       for i in self.store.good_dict.keys():
           if self.store.good_dict[i]==0:
               self.notif_list.append(i)
            
               
    def admin_menu(self):
        """[menu for admin]
        """
        while True:
            os.system("clear||cls")
            print('1-Show Notification')
            print('2-Add product to store')
            print('3-sign out')
            item = input('select item : ')
            if item =='1':
                os.system("clear||cls")
                print("______________All Notifications_____________")
                for n in self.notif_list:
                    print(f"the stock of the {n.name} has been finished!")
                input("press Enter to return...")
            elif item =='2':
                print("____________Here you can add a product to store_________________")
                print("For adding a new product you need to enter its specification ")
                g,n = self.add_good_to_store()
                # self.store.add_to_store(g,n)
                input("press Enter to return...")
            elif item=='3':
                break
