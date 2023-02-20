office_data={}

userchoice=input("how many user you want:")
for x in range(int(userchoice)):
    name=input("name:")
    position=input("position:")
    dob=input("dob:")
    temp = {}
    temp["dob"] = dob
    temp["position"]= position
    office_data[name]=temp
print(office_data)

while True:
    
    ask=int(input("do you want to make changes: update name = 1 \n update position =2 \n update dob =3\n"))
    
    if (ask==1):
        b = 'y'
        while b == 'y':
            update_name=input("which name you want to update?")
            x = input("Enter new name: ")
            office_data[x] = office_data[update_name]
            del office_data[update_name]
            print(office_data)
            b =input("do you want to update another name? (y/n) :")
            
    elif ask==2:
        b = 'y'
        while b == 'y':
            update_position=input("which key's position you want to update?")
            y = input("Enter new position: ")
            office_data[update_position]['position']=y
            print(office_data)
            b =input("do you want to update another position? (y/n) :")
            
    elif ask==3:
        b = 'y'
        while b == 'y':
            update_dob=input("which dob you need to change")
            z = input("Enter new dob: ")
            office_data[update_dob]['dob']=z
            print(office_data)
            b =input("do you want to update another dob? (y/n) :")

    else:
        print("you have entered wrong choice")    
        
