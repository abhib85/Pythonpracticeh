# List slicing
list = ["Harry", "Tom", "Rohan", "Sam", "Divya", 45]
list[0]=("garry")
list[1]=None
print(list)
list.remove(None)
print(list[0::])
print(list[::-1])
print(list)
#------------------------------------------------------------------
str="hello world"
print(str[0:])
print(str[::-1])
print(str)
#str.replace("h","p")---doesnt work
str=str.replace("h","p")
print(str)
#str[0]="s"=TypeError: 'str' object does not support item assignment
print(str)

#-----------------------------------------------

tuple=(1,2,3)
#print(type(tuple))
print(tuple[::-1])

#----------------------------------------
set={1,'x',2,3,4,5}
print(type(set))
print(set)
#add=set.add("added item")---doesnt work
set.remove("x")
set.add("y")
print(set)


#--------------------------------
dict={"key1":"value1","key2":"value2"}
print(dict)
#print(dict[0])
#print(dict.key1)===AttributeError: 'dict' object has no attribute 'key1'
#print(dict.keys)===<built-in method keys of dict object at 0x0000024509CC2A80>
print(dict.keys())
print(dict.values())


#Adding new key values to dict


#dict.add("key3":"value3")====SyntaxError: invalid syntax
#dict.add{"key3":"value3"}====SyntaxError: invalid syntax
#dict=dict.add({"key3":"value3"})===doesnt work

#Adding new key values to dict
dict["key3"]="value3"
print(dict)

#dict.remove["key3"]===doesnt work
print(dict)

# Create a Python dictionary
sixMonths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30}

print("Delete a specific element")
print(sixMonths.pop(6))
print(sixMonths)

print("Delete an random element")
sixMonths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30}
print(sixMonths.popitem())
print(sixMonths)

print("Remove a specific element")
del sixMonths[5]
print(sixMonths)

print("Delete all elements from the dictionary")
sixMonths.clear()
print(sixMonths)

# Finally, eliminate the dictionary object
del sixMonths
print(sixMonths)


