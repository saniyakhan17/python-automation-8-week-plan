#sets
#it has no duplicate values
# its unordered collection of data
# cannot be accessed using an index
set1={1,2,3,4,5}

s1={0,2,4,6,8,24,10}
s2={0,1,3,5,7,24,45,33}
print("Union of two sets:" + str(s1 | s2))
print("Intersection of two sets:" + str(s1 & s2))
print("Difference of two sets:" + str(s1 - s2))
print("Symmetric difference of two sets:" + str(s1 ^ s2))
