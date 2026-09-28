#COMPARISION OPERATORS
# == : equal to
# != : not equal to
# > : greater than
# < : less than
# >= : greater than or equal to
# <= : less than or equal to

# print(5==5) # prints True
# print(5!=5) # prints False
# print(5>3) # prints True
# print(5<3) # prints False
# print(5>=5) # prints True
# print(5<=5) # prints True

#LOGICAL OPERATORS
# and : returns True if both statements are true
# or : returns True if one of the statements is true
# not : reverses the result, returns False if the result is true

# print(5>3 and 5<10) # prints True
# print(5>3 or 5>10) # prints True
# print(not(5>3)) # prints False
# print('vanilla'>'chocolate') # prints False

# MEMBERSHIP OPERATORS
# in : returns True if a sequence with the specified value is present in the object
# not in : returns True if a sequence with the specified value is not present in the object
ice_cream="I love vanilla ice cream"
print('vanilla' in ice_cream) # prints True
print('vanilla' not in ice_cream) # prints False

a=[1,2,3,4,5]
print(1 in a)
print(6 not in a)
print(3 not in a)
