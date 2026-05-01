# dictionary - key-value pair, unordered, mutable

mydict = {"name" : "Hari", "age" : 21, "class" : "17th"}
print(mydict)

value = mydict["name"]
print(value)

mydict["email"] = "hari@gmail.com"
print(mydict)

del mydict["email"]
print(mydict)

mydict.pop("class")
print(mydict)

if "name" in mydict:
    print(mydict["name"])

else:
    print("thapu panita singaram") # try and except can be used also

for value in mydict.values():
    print(value)

for key in mydict.keys():
    print(key)

mydict2 = mydict
mydict2['fav'] = "dosa"

print(mydict)
print(mydict2)