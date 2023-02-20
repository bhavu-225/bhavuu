data={}
z=input("user defined")
for x in range(int(z)):  
    name=input("name:")
    dob=input("dob:")
    age=input("age:")
    year=input("year:")
    dict={"name":name,
        "dob":dob,
        "age":age,
        "year":year}
    data.update(dict)
choice = int(input("do you want to (1) add/update an name to the dictionary or (2) remove an name: (1 or 2):  "))
# for z in data:  
if choice in [1,2]:
        if choice == 1:
            data[input("key: ")] = input("value: ")
        else:
            data.pop(input("key: "))
# else:
#         print("invalid choice")
# print(z)        
print(data)