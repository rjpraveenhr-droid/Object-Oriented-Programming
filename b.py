class student:
    school="ABC" #global variable : common for all objects
    def __init__(self,r,n,g):#constructor
        self.rno=r
        self.name=n
        self.grade=g
    def intro(self):
        print("Hi this is", self.name, "from", self.school, "school, Roll number =", self.rno)
    def det(self):
        print("I study in grade", self.grade)

o1=student(16,"Arnold",11)
o1.intro()
o1.det()
o2=student(14,"lohisree",9)
o2.intro()
o2.det()
        