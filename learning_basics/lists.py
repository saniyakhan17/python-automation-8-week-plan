# lISTS
# my_list = [1, 2, 3, 4, 5]
# print(my_list) # prints [1, 2, 3, 4, 5]
#it is also indexed
#we can put any data type here


list1=[1,'cat', 3.5, True, [1,2,3], (1,2,3)]
#update or change the value of a list
list1[4]=23
# print(list1) # prints [1, 'cat', 3.5, True, 23, (1, 2, 3)]
#appending to a list
#one way to append to a list is using the append() method
list1.append('dog')
#print(list1)
list1[6]='new_value'
#print(list1) # prints [1, 'cat', 3.5, True, 23, (1, 2, 3), 'new_value']

#nested list
# we already saw that we can have a list inside a list, this is called a nested list
nested_list = [1, 2, [3, 4], [5, 6, [7, 8]]]
# we can access the elements of a nested list using multiple indices    
nested_list[2][0] # prints 3
