import pandas as pd
import hashlib
import csv
import time
import os
from store_class import Store
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,filename='store_logs.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
class User:
    """[this class belongs to users]
    """
    def __init__(self, username, password, status=None):
        """[constructor of user class]

        Args:
            username ([str]): [username of each user obj]
            password ([str]): [pass of each user obj]
            status ([boolian]) : [0 means lock and 1 means active]
        """
        self.username = username
        self.password = password
        self.status = status
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
                logging.error("invalid password")
            else:
                password_ = password
                break

        hash_password = hashlib.sha256(password_.encode("utf8")).hexdigest()
        obj_user = User(username_, hash_password,1)
        

        row_account = [[obj_user.username, obj_user.password , 'user',obj_user.status]]
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
        df_account = pd.read_csv(file_path)
        u_list = df_account['username']
        p_list = df_account['password']
        s_list = df_account['status']

      
        # index = 1
        for u,p,s in zip(u_list,p_list,s_list):
            if username == u :
                if s != 0:
                    
                    for i in range(3):
                        password = input(f"enter your password (try {i+1}):")
                        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
                        
                        if hash_password == p:
                            return User(u,p ,1)
                    else:
                        print("your account has been locked due to 3times wrong login information")
                        user_list=list(u_list)
                        index=user_list.index(u)
                        df_account.at[index , 'status'] = 0
                        df_account.to_csv(r'account.csv', index = False)
                else:
                    print("your account has been locked")
                    print("\n You can try to login later whenever admin unlocks your account")
                    input("\n press any key to return ...")
                    return 'False'
                    
        #TODO : handle the exeption of do not making object in login?    
        else:
            return None

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
    
    def calculate_bill(self):
        """[just calculate the bill]

        Returns:
            [int]: [sum of the whole shopping items]
        """
        sum = 0
        for g in self.order_dict.keys():
            sum = sum + g.price *self.order_dict[g]
        return sum 

    def save_bill_to_file(self):
        """[summary]

        Args:
            obj_user ([type]): [object of user]
        """

        file_path = "orders.csv"
        df_account = pd.read_csv(file_path)
        order_details =''
        for g in self.order_dict.keys():
            order_detail = f'{g.name} : {g.price}| '
            order_details = order_detail +order_details
        total_price = self.calculate_bill()    
        date = datetime.now()
        row_account = [[self.username,order_details,total_price ,date]]
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)

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
            
            try:
                os.system("clear||cls")
                print(f"_________________Wellcome {self.username}____________________ ")
                print("login ---->user main menu")
                print('1-show me the products of store')
                print('2-show my bill')
                print('3-sign out')
                item = input('select item : ')
                if item =='1':
                    while True:
                    
                        os.system("clear||cls")
                        print("______________Products of store_____________")
                        print("login ---->user main menu ----> show products")
                        self.store.show_products()
                        product_index = input("Select item or press Enter to submit order and back to menu: ") 
                        
                        try:
                            g = self.store.get_good_by_index(int(product_index))
                        
                            number_of_order=int(input(f"How many of {g.name} you want? "))
            
                            ##TODO: chera print ba vojude sleep bazam zud mire?
                            if self.store.remove_from_store(g,number_of_order):
                                print("your order has been successfuly added!")
                                time.sleep(2)
          
                                try:
                                    self.order_dict[g] = self.order_dict[g] + number_of_order
                                except:
                                    self.order_dict[g] = number_of_order

                            else:
                                print("lack of product")
                                logging.warning("lack of product")
                                time.sleep(2)
                                
                        except:
                            if product_index ==''and self.calculate_bill()!=0:
                                self.save_bill_to_file()
                                break
                            else:
                                print("invalid input")
                                logging.error("invalid input error in choosing products")
                                time.sleep(2)
                    
                elif item =='2':
                    print(f"login ------>user main menu ------> show {self.username} bill")
                    # print(f'your bill = {self.calculate_bill()}')
                    self.print_bill()
                    logging.info("New bill has been added")
                elif item=='3':
                    break
            except:
                print('invalid input')
                logging.error("an error happened in user menu")

    
    



        


    

        


