#take value of n
no_of_students = int(input(" "))
#create empty list
records = []
#append record of each student name,score in a for loop
for i in range(no_of_students):
    name = input()
    score = float(input())
    records.append([name, score])

#convert list of records to a python dictionary
# [['Harry', 37.21], ['Berry', 37.21]] becomes 
# {'Harry': 37.21, 'Berry': 37.21}
records = dict(records)
#get only values from our dictionary and use set function to rmeove duplicate score then sort it in ascending order
scores = sorted(set(records.values()))
#index 1 has the 2nd lowest score
second_lowest_score = scores[1]
#create a list of names of students who has 2nd lowest score using list comprehension
second_lowest_students = [name for name,score in records if score==second_lowest_score]
#sort names in alphabetical order
second_lowest_students.sort()
#loop through each name and print
for name in second_lowest_students:
    print(name)