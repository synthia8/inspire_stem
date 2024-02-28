# this is a program to solve surface area of a cylinder
# name : synthia wangui 
# date : 20/02/2024

r = float(input("enter the radius"))
h = float(input ("enter the height"))
d = float( input("enter the diameter"))

pi = 3.142


x = (pi * (r**2) * h)  + (2 * pi * d)
print ("the surface area of the cylinder is",x)