class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)



s1 = Student("Prajit", 20, "IT")
s2 = Student("Messi", 36, "Football")


s1.display()
print()
s2.display()
