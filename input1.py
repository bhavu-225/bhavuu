class employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def show_employee_detail(self):
        a=input("name of employee:")
        b=input("age of employee:")
        c=input("salary of employee:")
        d=input("gender of employee:")
        
p1=employee("a","b","c","d")
p1.show_employee_detail ()  
# -----------------------------------------
# 
# a=int(input("value1:"))
# b=int(input("value2:"))
# z=int(input("select operation\npress 1 for add\npress 2 for subs\npress 3 for mul\npress 4 for division"))
# print(a)
# print(b)
# print(z)
# if z == 1:
#     print(a + b)
# elif z == 2:
#     print(a - b)
# elif z == 3:
#     print(a * b)
# elif z == 4:
#     if a==0 or b==0:
#         print("please enter a valid value")
#     else:
#          print(a / b)
# else:
    # print("select valid operation")
# 
# data=[]
# z=input("user defined")
# for x in range(int(z)):  
#     name=input("name:")
#     dob=input("dob:")
#     age=input("age:")
#     year=input("year:")
#     dict={"name":name,
#         "dob":dob,
#         "age":age,
#         "year":year}
#     data.append(dict)
# print(x)
# print(data)
# z1=input("user defined")
# for rec in data:
#     if z1 != rec["name"]:
#         print(rec["age"])
    

    # else:
        # print("u got d name have fun")


