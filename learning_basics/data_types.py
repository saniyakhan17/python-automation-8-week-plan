# #DATA TYPES IN PYTHON   - STRINGS (STR)

#print(type(12))
#print(type(12.5))
#print(type("Hello"))
#print(type(True))
#print(type(False))
#print(type(12+3j))
#print(type([1,2,3,4,5]))
#print(type(1>5))
#print(type(1==1))


#STRINGS

#enclosed in '' or "" or """ """
x='hello'
#y='Sana is Saniya's sister' #this will give an error because of the single quote in the string
y="Sana is Saniya's sister" #this will not give an error because of
#same usage for double quotes, and triple quotes can be used for multi-line strings
song ="""Buddy you are a boy 
make a big noise
playing on a the street 
gonna be a big man some day
"""
# the above string is a multi-line string and can be printed as it is
#print(song)

# strs can be indexed
temp="Hello World"
# print(temp[0]) # prints H
# print(temp[-1]) # prints d      
# print(temp[0:7]) # prints Hello W

#strings are immutable, we cannot change the value of a string once it is created
#slices can be used to create a new string from an existing string
#string[start:stop:step]
# s = "Hello, Saniya!"

# print(s[0:5])      # Hello        -> from index 0 to 4
# print(s[7:13])     # Saniya       -> from index 7 to 12
# print(s[:5])       # Hello        -> start omitted, defaults to 0
# print(s[7:])       # Saniya!      -> stop omitted, goes to the end
# print(s[:])        # Hello, Saniya!  -> full copy of the string
# print(s[-7:-1])    # Saniya       -> using negative indices
# print(s[::2])      # Hlo ai!      -> every 2nd character
# print(s[::-1])     # !ayinaS ,olleH  -> reverses the string

#we can also multiply strings with integers to repeat them
# a='rubber'
# print(a*3) #rubberrubberrubber
# print(a*0) #prints nothing
# print(a*-1) #prints nothing
# print(a+a) #rubberrubber
