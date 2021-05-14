import pandas as pd
import logging
from datetime import datetime
import time

# logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG, filename='app.log',filemode='a',format='%(levelname)s-%(asctime)s -%(message)s',datefmt='%d-%b-%y %H:%M:%S')


df = pd.read_csv('account.csv')

uu = df['username']
pp = df['password']
rr = df['roll']

# print(df)
# u = uu[3]
# print(u)
# user_list=list(uu)
# index=user_list.index(u)
# print(index)
# print(user_list)
# df.at[index , 'status'] = 0
# df.to_csv(r'account.csv', index = False)

# df.set_value(1, "roll", 'aaaaaaaa')
# print(df)
# df.at[3,'roll']='aaaaaaaa'
# # print(df)
# df.to_csv(r'account.csv', index = False)


for  i,(s,r) in enumerate(zip(uu,rr ,pp)):
    print(f"{i+1} : {s} {r}")

# for u,p ,r in zip(uu,pp ,rr):
#     print(u,p,r)



class User:
    def __init__(self,name , status = None):
        self.name = name
        self.status = status

    @staticmethod
    def login():
        a = input ("enter username:")
        user_obj = User(a) 
        
        return user_obj  
    def set_account_lock(self):
        """[lock the account due to 3times worng login info]

        Args:
            user ([type]): [user obj]
        """
        self.status = 0
        return self.status

obj = User.login()
logging.info('This will get logged to a file')
ii = 0
while True:
    logging.error(f'error messsage {ii}')
    time.sleep(1)
# obj.set_account_lock()
# print(obj.status)
# print(datetime.now())