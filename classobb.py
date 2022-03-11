class Mom:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printDetails(self):
        print(self.name+"\n"+self.age)

child = Mom("sumanth","21")
child.printDetails()