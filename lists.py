#Python data types

# A list is a collection which is ordered and changeable, Allows Duplicate members. 

# create list

numbers = [1, 2, 3 ,4 ,5]

# using a constructor
numbers = list((1, 2, 3 ,4 ,5))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Get value
print(fruits)

# get len 
print(len(fruits))

#append to list
fruits.append('Mangos')

#remove from list
fruits.remove('Grapes')

#insert into position
fruits.insert(2, 'Strawberries')

print(fruits)