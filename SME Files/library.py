class Library:
    def __init__(self, name, pages, stock):
        self._name = name
        self._pages = pages
        self._stock = stock
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_pages(self):
        return self._pages
    def set_pages(self, pages):
        self._pages = pages
    def get_stock(self):
        return self._stock
    def set_stock(self, stock):
        self._stock = stock
    def display_info(self):
        print("Name:", self.get_name(), "Pages:", self.get_pages(), "Stock:", self.get_stock())
book1 = Library("Python Basics", 200, 5)
book2 = Library("Data Science", 350, 3)
book3 = Library("Machine Learning", 400, 2)
book1.display_info()
book2.display_info()
book3.display_info()

