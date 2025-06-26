class Employee:
    def __init__(self, name, emp_id, salary):
        self._name = name
        self._emp_id = emp_id
        self._salary = salary
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_emp_id(self):
        return self._emp_id
    def set_emp_id(self, emp_id):
        self._emp_id = emp_id
    def get_salary(self):
        return self._salary
    def set_salary(self, salary):
        self._salary = salary
    def display_info(self):
        print("Name:", self.get_name(), "ID:", self.get_emp_id(), "Salary:", self.get_salary())
emp1 = Employee("Alice", 101, 50000)
emp2 = Employee("Bob", 102, 60000)
emp3 = Employee("Charlie", 103, 55000)
emp1.display_info()
emp2.display_info()
emp3.display_info()
