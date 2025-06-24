class Employee:
    next_id = 1  # Class variable to assign unique IDs

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.id = Employee.next_id  # Assign current ID
        Employee.next_id += 1       # Prepare next ID

    def display(self):
        print(f"Employee #{self.id}: {self.name}, {self.position}")

e1 = Employee("AG", "CEO")
e2 =  Employee("JEROW", "PRESIDENT")

e1.display()
e2.display()