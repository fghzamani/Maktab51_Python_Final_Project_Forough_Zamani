import hashlib
import json
from Admin_class import Admin
from User_class import User
import os
import time
class LoginSystem:
    """
        [this class can handle the login and registration process]
    """
    def __init__(self,db_filename):
        """

        Args:
            db_filename ([json file]): [this file contains all the names and passwords hash]
        """
        self.db_filename = db_filename
        self.user_list = []
        self.admin_list = []
        self.current_user = None    # admin or user 
        self.load_file(db_filename)

    def load_file(self , filename):
        """[this method load the file of information]

        Args:
            filename ([json]): [description]
        """
        try:
            with open(filename) as json_file:
                data_dict = json.load(json_file)
                admin_list = data_dict['admin']
                user_list = data_dict['user']
                
                for p in admin_list:
                    name = p['name']
                    password = p['password']
                    admin_ = Admin(name , password)
                    self.admin_list.append(admin_)
                for u in user_list:
                    name = u['name']
                    password = u['password']
                    user_ = User(name,password) 
                    self.user_list.append(user_)
        except:
            self.save_file()
    

    def save_file(self):
        """[this method saves the objects of admin and users in  json file]
        """
        tmp_dict = dict()
        user_list =[]
        admin_list = []
        for user in self.user_list:
            user_dict = dict()
            user_dict['name'] = user.name
            user_dict['password'] = user.password
            user_list.append(user_dict)
        
        for admin in self.admin_list:
            admin_dict = dict()
            admin_dict['name'] = admin.name
            admin_dict['password'] = admin.password
            admin_list.append(admin_dict)
        tmp_dict = {'admin':admin_list , 'user':user_list}

        with open(self.db_filename, 'w') as outfile:
            json.dump(tmp_dict, outfile)

    def hash_pass(self,password:str) :
        """[this method hashes the passwords]

        Args:
            password (str): [description]

        Returns:
            [str]: [hashed password]
        """
        return str(hashlib.sha256(password.encode('utf-8')).hexdigest())

    def registration(self,name,password,roll):
        """[summary]

        Args:
            name ([type]): [description]
            password ([str]): [description]
            roll ([type]): [description]
        """
        
        pass_hash = self.hash_pass(password)
        if roll =='admin':
            a = Admin(name , pass_hash)
            self.admin_list.append(a) 
        elif roll =='user':
            a = User(name , pass_hash)
            self.user_list.append(a) 
            
        self.save_file()

    def sign_in(self, name, password):
        """[this method can sign in users]

        Args:
            name ([str]): [name of user or admin]
            password ([str]): [password of account]

        Returns:
            [object]: []
        """
        hash_pass = self.hash_pass(password)
        for u in self.user_list + self.admin_list:
            if name == u.name and hash_pass == u.password :
                self.current_user = u 
                return u

        return None
            

    def sign_out(self):
        """[this method can sign out from the account]
        """
        self.current_user = None
        


    def user_interface(self):
        """ command line interface 
        """
        counter=0
        while True:
            os.system("clear||cls")
            print("_________________________Wellcome to fgh store__________________________")
            print("________________________________________________________________________")
            if self.current_user != None:
                print(f"Hi {self.current_user.name}. you just have login successfully !")
                print("1. sign out")
                print("2. back to menu")
                i= input("Select item")
                if i =='1':
                    self.sign_out()
                else:
                    return self.current_user
            else:
                
                account = input("\n if you dont have account, you need to register,Do you have account? Y/n ")
                if account == 'y' or account =='Y':
                    print("So login to your account")
                    name = input("please enter your name: ")
                    password = input('please enter your password :')
                    u = self.sign_in(name , password)
                    if u == None:
                        print("Your name or password is not correct!")
                        counter = counter +1
                
                    else:
                        print(f"Hi {name}. you just have login successfully !")
                    time.sleep(2)
                    if counter ==3:
                        print("Your access  has been denied due to three times of entering wrong username or password")
                        return self.sign_out()
                                    
                elif account == 'N' or account == 'n':
                    print("So you can sign up here")
                    print(" you have to inform your roll")
                    print("1.Admin")
                    print("2.User")
                    roll = input("Select your roll:")
                    if roll =='1':
                        roll_type = 'admin'
                    else:
                        roll_type = 'user'
                    name = name = input("please enter your name: ")
                    password = input('please enter your password :')
                    self.registration(name , password , roll_type)
                
                    k = input("\n \npress Enter to return to menu ...")
            

