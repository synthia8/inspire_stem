laptop ={"make":"lenovo","colour":"black","weight":"1.2","year":"2020"}


print(laptop["make"])
print(laptop["colour"])
print(laptop["year"])

laptop["colour"]="red"
laptop["year"] ="2005"
'''

for key,value in laptop.items():
    print (key)
    print("\n")
    print(value)
'''
laptop["size"] ="1200mm x 600mm"
print (laptop)

del laptop ["colour"]
print (laptop)

siz_laptop = laptop.cop()
print(siz_laptop)
