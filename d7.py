# class triangle:
#     def __init__(self,a,b,c,h):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.h=h
#     def get_perimeter(self):
#             x = (self.a + self.b + self.a )
#             print(x)
#     def get_area(self):
#             y =self.h*self.b / 2
#             print(y)
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c"))
# h=float(input("h=") )           
# t=triangle(a,b,c,h)
# t.get_perimeter()
# t.get_area()
# ----------------------------------------------------
# class triangle:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c   
# class triangle1(triangle):
#         def __init__(self,a,b,c,h):
#             super().__init__(a,b,c)
#             self.h=h
#         def get_perimeter(self):
#             self.get_perimeter
#             s=self.a + self.b + self.c 
#             print(s)
#         def get_area(self):
#             self.get_area
#             z=self.h* self.b/2
#             print(z)
            
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# h=float(input("h="))
# t=triangle(a,b,c)
# t1=triangle1(a,b,c,h)
# t1.get_perimeter()
# t1.get_area()
# ---------------------------------------------
class triangle:
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3   
class triangle1(triangle):
        def __init__(self,side1,side2,side3,height):
            super().__init__(side1,side2,side3)
            self.height=height
        def get_perimeter(self):
            s=self.side1 + self.side2 + self.side3 
            print(s)
        def get_area(self):
            b = self.side1 + self.side2 + self.side3 
            z=(b*(b-side1)*(b-side2)*(b-side3))** 0.5
            print(z)
            
            
side1=float(input("side1="))
side2=float(input("side2="))
side3=float(input("side3="))
height=float(input("height="))
t=triangle(side1,side2,side3)
t1=triangle1(side1,side2,side3,height)
t1.get_perimeter()
t1.get_area()