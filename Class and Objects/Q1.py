#Create a sample class named Employee with two attributes id and name
#employee :
    #id
    #name
#object initializes id and name dynamically for every Employee object created.

#emp = Employee(1, "coder")

class Employee:

    def __init__(self, id, name): #Properties
        self.id = id
        self.name = name

    def display(self): #Methods
        print(f"ID: {self.id} \nName: {self.name}")


# Creating a emp instance of Employee class
emp = Employee(1, "coder")

emp.display()

    

    
