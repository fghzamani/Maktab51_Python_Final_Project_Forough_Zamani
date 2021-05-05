import pandas as pd
import hashlib
import csv
import time
import os
from store_class import Store
class User:
    """[this class belongs to users]
    """
    def __init__(self, username, password ):
        """[constructor of user class]

        Args:
            username ([str]): [username of each user obj]
            password ([str]): [pass of each user obj]
        """
        self.username = username
        self.password = password
        self.user_list=[]
        self.roll='user'
        self.order_dict = dict()


    @staticmethod
    def register():
        """[method for  user registeration]
        """
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account["username"])
        username_ = ''
        password_ = ''
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
        obj_user = User(username_, hash_password)
        

        row_account = [[obj_user.username, obj_user.password , 'user']]
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)

    @staticmethod
    def login():
        """[this method handles user login]

        Returns:
            [obj]: [object of user or none]
        """
        file_path = "account.csv"
        username = input("enter your username:")  
        password = input("enter your password:")
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
        df_account = pd.read_csv(file_path)
        u_list = df_account['username']
        p_list = df_account['password']

        for u,p in zip(u_list,p_list):
            if username ==u and hash_password ==p :
                return User(u,p)
        else:
            return None

    def calculate_bill(self):
        """[just calculate the bill]

        Returns:
            [int]: [sum of the whole shopping items]
        """
        sum = 0
        for g in self.order_dict.keys():
            sum = sum + g.price *self.order_dict[g]
        return sum 

    def print_bill(self):
        """[calculate and print the bill with each item]

        Returns:
            [int]: [sum of the whole shopping items]
        """
        sum = 0
        for g in self.order_dict.keys():
            print(f"{g.name} :{g.price} *{self.order_dict[g]} ")
            sum = sum + g.price *self.order_dict[g]
        print(f"\nyour bill = {sum}")
        input("press Enter to return ....")

    def set_store(self,store):
        """[set the store for user]

        Args:
            store ([obj]: [description]
        """
        self.store = store
            
    def user_menu(self):
        """[menu for user]
        """
        while True:

            print('1-show me the products of store')
            print('2-show my bill')
            print('3-sign out')
            item = input('select item : ')
            if item =='1':
                os.system("clear||cls")
                print("______________Products of store_____________")
                self.store.show_products()
                product_index = input("Select item or press Enter to back to menu: ") 
                ##TODO: handle valid index
                g = self.store.get_good_by_index(int(product_index))
                number_of_order=int(input(f"How many of {g.name} you want? "))
                ##TODO: handle ....
                if self.store.remove_from_store(g,number_of_order):
                    print("your order has been successfuly added!")
                    try:
                        self.order_dict[g] = self.order_dict[g] + number_of_order
                    except:
                        self.order_dict[g] = number_of_order

                else:
                    print("lack of product")
                    
                
            elif item =='2':
                # print(f'your bill = {self.calculate_bill()}')
                self.print_bill()
            elif item=='3':
                break
    
    



        


    

        


