# a program to run dictionaries
# name : synthia wangui
# date : 28/02/2024

car = {"model":"mercides benz","colour":"black","cost":"8.5 million","exhausters":"two","seats":"foursitter"}
print (car["model"])
print (car["colour"])
print(car["cost"])
print(car["exhausters"])
print(car["seats"])

for key,value in car.items():
    print(key)
    print("\n")
    print(value)