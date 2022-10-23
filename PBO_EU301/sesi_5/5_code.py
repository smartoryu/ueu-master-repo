class Product:
    # Constructor
    def __init__(self, __mProductID, __mProductName, __mProductPrice, __mProductStock):
        self.__mProductID = __mProductID        # private attribute
        self.__mProductName = __mProductName    # private attribute
        self.__mProductPrice = __mProductPrice  # private attribute
        self.__mProductStock = __mProductStock  # private attribute

    # getter for private attribute __mProductID
    def getProductID(self):
        return self.__mProductID

    # getter for private attribute __mProductName
    def getProductName(self):
        return self.__mProductName

    # getter for private attribute __mProductPrice
    def getProductPrice(self):
        return self.__mProductPrice

    # getter for private attribute __mProductStock
    def getProductStock(self):
        return self.__mProductStock

    # setter for private attribute __mProductID
    def setProductID(self, __mProductID):
        self.__mProductID = __mProductID

    # setter for private attribute __mProductName
    def setProductName(self, __mProductName):
        self.__mProductName = __mProductName

    # setter for private attribute __mProductPrice
    def setProductPrice(self, __mProductPrice):
        self.__mProductPrice = __mProductPrice

    # setter for private attribute __mProductStock
    def setProductStock(self, __mProductStock):
        self.__mProductStock = __mProductStock

    # method to display product information
    def print(self):
        print(f"{self.getProductID():<10}{self.getProductName():<20}{self.getProductPrice():<10}{self.getProductStock():<10}")


product1 = Product("P001", "Apple", 10000, 10)
product1.print()
