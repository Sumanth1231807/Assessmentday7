class Parent():
    def __init__(self, name, age, phoneno):
        self.name = name
        self.age = age
        self.phoneno = phoneno

    def displayDetails(self):
        print("self.name"+"\n"+"self.age"+"\n"+"self.age"+"\n"+self.phoneno)

class Child(Parent):
    def __init__(self, name, age, phoneno, child_name, child_age, child_number):
        self.child_name = child_name
        self.child_age = child_age
        self.child_number = child_number

        Parent.__init__(self,name, age, phoneno)

    def printDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone_number:", self.phoneno)
        print("Child_name:", self.child_name)
        print("Child_age:", self.child_age)
        print("child Phone number:", self.child_number)

x = Child("sumanth","21","9677312849","prince", "21", "9545378354")
x.printDetails()
x.displayDetails()
y = Parent("streak", "50", "9677312078")