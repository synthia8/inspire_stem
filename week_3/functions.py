# this is a program to solve functions
# name : synthia wangui
#date : 29/02/2023

def print_name ():
    print("my name is synthia wangui")
# calling the function
print_name()
print_name()
print_name()
print_name()

# print details
def print_details(name,age,id,gender):
    print("i am{0},i{1}years old,my id number is{2},my gender is{3}".format (name,age,id,gender))

    #calling the function
print_details("synthia wangui","19","29876065","female")
print_details("john","20","23467789","male")
 
# sum of numbers
def sum_nums(x,y):
    return x+y

z = sum_nums (10,20)
print(z)

#product of numbers...how to define fucti
def prod_nums(x,y):
    return x*y
print(prod_nums(4,9))# you dont have to assign into another variable
