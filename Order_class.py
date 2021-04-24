from Good_class import Good

class Order:

    def __init__(self,name_of_client,number):
        """[this class is for ordering good]

        Args:
            name_of_client ([str]): [name of user ]
            number ([int]): [number of a good that want to order]
        """

        self.name_of_client = name_of_client
        self.good_list = []
        self.number = number
        self.bill=[]

    def add_good(self,g:Good):
        """[summary]

        Args:
            g (Good): [object of good]
        """
        print("This method is going to add a chosen good for a user in its sabade kharid")

    def calculate_bill(self):
        print('this method can calculate the bill')
    
    def show_bill(self):
        print('this method is going to show the bill of client')
