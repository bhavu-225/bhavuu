# enter student name,enroll n append that into list
class student:
    def __init__(self,name,enroll):
        self.name=name
        self.enroll=enroll
    def myfun(self):
        print("name:",self.name)
        print("enroll:",self.enroll)
list_of_student=[]
for x in range(3):
    name=input("enter your name:")
    enroll=int((input("enter your enroll:")))
    obj=student(name,enroll)
    list_of_student.append(obj)
else:
    print(list_of_student)
for i in list_of_student:
      i.myfun()
print(i)

