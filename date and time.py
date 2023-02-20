from datetime import datetime
today = datetime.today()
d1 = today.strftime("%d/%m/%Y")

print("date =", d1)
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
print("time =", dt_string)

# ---------------------------------------------

l = [9,5,1,3,7,8,4,2,10,6,0]

l.sort()
print(l)

l.sort(reverse=True)
print(l)

# ---------------------------------------------------------------


lst = [{"id" : 4, "name": "Manjit" },{"id" : 3, "name": "Bhavii" },{"id" : 2, "name": "Harsh" },{"id" : 1, "name": "Themsy" },{"id" : 6, "name": "Preeti"},{"id" : 5, "name": "Rehmat"}]

print(sorted(lst, key=lambda i: i["id"]))

print(sorted(lst, key=lambda i: i["id"] , reverse=True))
