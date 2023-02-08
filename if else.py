# #if else
# a=20
# b=30
# if b>a:
#     print("B is greater than A")
# # --------------------------------
# a=10
# b=20
# c=30
# if(a>b) & (a>c):
#     print("a is the greatest")
# elif(b>a) & (b>c):
#     print("b is the greatest")
# else:
#     print("c is the greatest")
# # --------------------------------------
# #if with tuple
# tup1=('a','b','z')
# if c in tup1:
#     print("c is present in tupe1")
# else:
#     print("c is not present in tup1")
#     # ---------------------------------
# #if with list also chnged d value frm b to z
# list1=['a','b','c'] 
# if list1[1]=='b':
#     list1[1]='z'
#     print(list1)
#     # -----------------------------------
# #  if with dictionary aldo chngede d vlue of k3 
# d1={'k1':10,'k2':20,'k3':60}
# if d1['k3']==60:
#     d1['k3']=d1['k3']+50
#     print(d1)
# #while 
# i=1
# while i<=10:
#     print(i)
#     i+=1
# # ---------------
# #table of 3 by while
# i=1
# n=3
# while i<=30:
#     print(n," * ",i," = ", n*i)
#     i=i+1
# #--------------------
# #table of 7 by while
# i=1
# n=7
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1
#     # ----------------
# #while with list added digit to form new value
# l1=[1,20,31,48,5,6]
# i=0
# while i<len(l1):
#     l1[i]=l1[i]+90
#     i+=1
#     print(l1)
# # -------------------------------------------------
# l2=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<len(l2):
#     i+=1
#     print(l2)
#for loop print individual element
l1=["apple","mango","cherry","kiwi"]
for x in l1:
    print(x)
# ---------------------------
#print single single element using for loop
l2=[1,2,3,4,5,6,7,8,9,10]
for x in l2:
    print(x)
 # --------------------
#  nested for loop
l1=["orange","black","white"]
l2=["cat","dog","horse"]
for x in l1:
    for y in l2:
        print(x,y)
# -------------------------
l1=[1,2,3]
l2=["cat","dog","horse"]
l3=["black","cute","slim"]
for x in l1:
    for y in l2:
        for z in l3:
            print(x,y,z)