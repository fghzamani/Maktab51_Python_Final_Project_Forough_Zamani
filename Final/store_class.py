import pandas as pd
import csv
from good_class import Good
class Store:
    def __init__(self):
        """[this class holds the whole information of goods in store]
        """
        self.name = 'fgh store'
        self.good_dict=dict()

    def save_repository(self):
        """[save changes in store into a csv file]
        """
        file_path = "repository.csv"
        df_account = pd.read_csv(file_path)
        rows_good = [["name" , "barcode" , "brand" , "price" , "number" ]]
        for good in self.good_dict.keys():
            rows_good.append([good.name,good.barcode,good.brand,good.price,self.good_dict[good]])
        
        with open(file_path, 'w', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(rows_good)

    def load_repository(self):
        """[load the repository of store]
        """
        file_path = "repository.csv"
        df_repository = pd.read_csv(file_path)
        name_list = df_repository['name']
        price_list = df_repository['price']
        barcode_list = df_repository['barcode']
        brand_list = df_repository['brand']
        number_list = df_repository['number']
        self.good_dict = {}
        for i in range(len(name_list)):
            product= Good(name_list[i],barcode_list[i],brand_list[i],price_list[i])
            # print("asrgdjgkjhtgb = " , product.name)
            # time.sleep(3)
            self.good_dict[product] = number_list[i]


        
    def add_to_store(self,good , number):
        """[adding good to store]

        Args:
            good ([good object]): [description]
            number ([int]): [number of good to add to store]
        """
        for i in self.good_dict.keys():
            if i.name == good.name :
                self.good_dict[i] = self.good_dict[i] + number
        else:
            self.good_dict[good] = number
        self.save_repository()

    def remove_from_store(self,good,request_number):
        """[remove from store with each shopping]

        Args:
            good ([obj]): [description]
            request_number ([int]): [number of good that a user wants to buy]

        Returns:
            [boolian]: [description]
        """
        for i in self.good_dict.keys():
            if i.name == good.name :
                if request_number <= int(self.good_dict[i]) :
                    self.good_dict[i] = self.good_dict[i] - request_number
                    self.save_repository()
                    return True
                    
                else:
                    return False

    def show_products(self):
        """[show whole product in store]
        """
        for i,g in enumerate(self.good_dict.keys()):
            print(f'{i+1}. {g.name} , {g.price}')
    
    def get_good_by_index(self,index):
        """[getting an index and return the good that refers to tha index ]

        Args:
            index ([str])

        Returns:
            [g]: [good object]
        """
        try:
            good_list = list(self.good_dict.keys())
            g = good_list[int(index)-1]
            print(g.name , index)
            return g
        except:
            return None
            
    def show_products_with_number(self):
        """[show product ]
        """
        for i,g in enumerate(self.good_dict.keys()):
            print(f'{i+1}. {g.name} , {g.price} , {self.good_dict[g]}')
