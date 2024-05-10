# a program on dictionaries
#name: synthia wangui
# date : 28/02/2024

car = {"model":"mercedes benz","colour":"black","cost":"8.5 million","exhausters":"two","seats":"foursitter"}

print (car["model"])
print (car["colour"])
print(car["cost"])
print(car["exhausters"])
print(car["seats"])

#for individual values
for key,value in car.items():
    print(key)
    print("\n")
    print(value)
