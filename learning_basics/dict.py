#dictionaries
#key value pair
#key indicates to what the value belongs to
dict1={"name":"John","age":30,"city":"New York"}
#print(dict1)
# print(dict1.values())
# print(dict1.keys())
# print(dict1.items())
# it is not indexed so how to access the values of a dictionary?
# we can access the values of a dictionary using the keys
# print(dict1["name"]) # prints John
# print(dict1.get("age")) # prints 30
dict1['name']="saniya"
# print(dict1)

# we can update like this as well
dict1.update({"age": 35})
dict1.update({"name":"John","age":30,"city":"New York", "status": "single"})

# to delete a pair
del dict1["status"]
print(dict1) # prints {'name': 'John', 'age': 30, 'city': 'New York'}