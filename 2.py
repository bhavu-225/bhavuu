#calculator
'''a will ask to enter a no., b will ask to enter second no.,
c will ask to enter our choice of operation, ans will store our result,
will apply if else condition for every operation in this calc.
at last applied one more condition that if our answer contains no. 2
it'll print a msg "your answer contains number 2" if not, it'll no display any msg'''

a = input("Enter first number: ")
b = input("Enter second number: ")
c = input("what do you want to do with this no.:(add/sub/mul/div)")
ans = 0

if c == "add":
    ans = int(a) + int(b)
    print(ans)
elif c== "sub":
    ans = int(a) - int(b)
    print(ans)
elif c == "mul":
    ans = int(a) * int(b)
    print(ans)
elif c == "div":
    if int(a) == 0 or int(b) == 0:
        print("choose other number")
    else:
        ans = int(a) / int(b)
        print(ans)
else:
    print("wrong choice")
    
if str(2) in str(ans):
    print("your ans contains 2")
else:
    print(" ")







