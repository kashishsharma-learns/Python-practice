from prettytable import PrettyTable

class Employee:
    def __init__(self,emp_id,name,age,salary,department,position,phone_number):
        self.emp_id=emp_id
        self.name=name
        self.age=age
        self.salary=salary
        self.department=department
        self.position=position
        self.phone_number=phone_number

    def __str__(self):
        return f"Id:{self.emp_id},Name:{self.name},Age:{self.age},Salary:{self.salary},Department:{self.department},Position:{self.position},Phone_number:{self.phone_number}"

class EmployeeManagementSystem:
    def __init__(self):
        self.employees=[]

    def add_employee(self):
      emp_id=input("Enter employee ID:")
      name=input("Enter employee name:")
      age=int(input("Enter employee age:"))
      salary=float(input("Enter employee salary:"))
      department=input("Enter employee department name:")
      position=input("Enter employee position:")
      phone_number=int(input("Enter employee number:"))

      employee=Employee(emp_id,name,age,salary,department,position,phone_number)
      self.employees.append(employee)
      print("\nEmployee added successfully\n")

    def view_employee(self):
        if not self.employees:
           print("\nNo employees to display\n")
           return

        #Create a PrettyTable object
        table=PrettyTable()

        #Define the column headers
        table.field_names=["Employee ID","Name","Age","Salary","Department","Position","Phone Number"]

        #Add employee data to the table
        for employee in self.employees:
             table.add_row([employee.emp_id,employee.name,employee.age,employee.salary,employee.department,employee.position,employee.phone_number])

        #Print the table
        print("\nList of Employees:\n")
        print(table)
        print()

    def search_employee(self,emp_id):
        #Search for the employee with the given emp_id
         for employee in self.employees:
            if employee.emp_id==emp_id:
                #Create a PrettyTable object
                table=PrettyTable()

                #Define the column headers
                table.field_names=["Employee ID","Name","Age","Salary","Department","Position","Phone Number"]

                #Add the found employee data to the table
                table.add_row([employee.emp_id,employee.name,employee.age,employee.salary,employee.department,employee.position,employee.phone_number])

                #Print the employee details in table form
                print("\nEmployee found:\n")
                print(table)
                return employee
         print("\nEmployee not found.\n")
         return None

    def update_employee(self): 
        emp_id=input("Enter the employee ID to update:")
        employee=self.search_employee(emp_id)
        if employee:
            print("Enter new details(press enter to skip a field):")
            name=input("Enter new name(leave blank to keep current):")
            age=int(input("Enter new age(leave blank to keep current):"))
            salary=float(input("Enter new salary(leave blank to keep current):"))
            department=input("Enter new department(leave blank to keep current):")
            position=input("Enter new position(leave blank to keep current):")
            phone_number=int(input("Enter new number(leave blank to keep current):"))
            
            if name:
                employee.name=name
            if age:
                employee.age=age
            if salary:
                employee.salary=salary
            if department:
                employee.department=department
            if position:
                employee.position=position
            if phone_number:
                employee.phone_number=phone_number

            print("\nEmployee details updated successfully\n")
            
    def delete_employee(self):
        emp_id=input("Enter the emp_id to delete:")
        employee= self.search_employee(emp_id)
        if employee:
            self.employees.remove(employee)
            print("\nEmployee deleted successfully\n")
        else:
            pass
        
def menu():
    system= EmployeeManagementSystem()

    while True:
        print("Employee Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice=input("Enter your choice:")

        if choice=="1":
            system.add_employee()
        elif choice=="2":
            system.view_employee()
        elif choice=="3":
            emp_id=input("Enter employee ID:")
            system.search_employee(emp_id)
        elif choice=="4":
            system.update_employee()
        elif choice=="5":
            system.delete_employee()
        elif choice=="6":
            print("Existing...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__=="__main__":
    menu()

                
                
            

    

        
        
