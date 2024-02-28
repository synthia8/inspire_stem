# name : synthia wangui
# date : 28/02/2024

friends = ["jane","ian","aron","brian","felix","austin"]
for friend in friends:
    print (friend)
    
enemies =friend[:] #copy one list into another 
print (enemies) 

fruits = ["lemon","guava","mango","apple","pineapple"]
#slice the list to get part of  the list 

print(fruits[0:3])

#cities
cities =("nairobi","mombasa","eldoret","")

del fruits[0]
print (fruits)

squares = [] #initializes an empty list

for x in range (0,11):
    squares.append(x**2)

print(squares)



