import math

def circle_calc(radius):
    Area = math.pi * ( radius ** 2 )   
    Circumference= 2 * math.pi *radius
    return Area,Circumference

a,c=circle_calc(2)

print("Area: ",round(a,2),"Circumference: ",round(c,2))


