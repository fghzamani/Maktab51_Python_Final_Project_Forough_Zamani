class Good:
    """[class for goods in store]
    """
    def __init__(self,name , barcode,brand,price):
        """[summary]

        Args:
            name ([str]): [name of product]
            barcode ([int]): [barcode of product]
            brand ([str]): [brand of product]
            price ([int]): [price of product]
        """
        self.name= name
        self.barcode=barcode
        self.brand=brand
        self.price=price