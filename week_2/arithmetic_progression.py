# this is a program to solve arithmetic progressions
# name: synthia wangui
# date:20/02/2024

# sum of ap 

a = float(input("enter first term"))
n = float(input("enter number of terms"))
d = float(input("enter the common difference"))

x = n/2 * ((2*a)+(n-1)*d)

print ("the sum of the arithmetic progression is:",x)

# n-terms of ap 

s = float(input(" enter the first term"))
p = float(input(" enter the number of terms"))
o = float(input(" enter the common difference"))

k = s + (p-1)*o

print ("the number of terms of the ap is:",k)


#sum of gp 
h = float(input("enter the first term "))
k = float(input("enter the common ratio"))
l = float(input("enter the number of terms"))

s = (h*(k**(l-1)-1))/(k-1)

print ("the sum of gp is:",s)

#number of terms of gp

j = float(input("enter the first term"))
f = float(input("enter the common ratio"))
b = float (input(" enter the number of terms"))

g = j * (f**(b-1))

print ("the number of terms of gp:",g)
          
