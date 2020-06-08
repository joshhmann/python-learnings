# a tuple is a collection which is ordered and immutable, Allows duplicate members.
#reat job, you understand the properties of a tuple! A tuple is an immutable, ordered data structure that can be indexed and sliced like a list. Tuples are defined by listing a sequence of elements separated by commas, optionally contained within parentheses: ().
#simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')

#using constructor 

#fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# get single value
print(fruit_tuple(1))

#cannot change value
fruit_tuple[1] = 'Grape'

#tuples with one value should have trailing comma

fruit_tuple_2 = ('Apple',)

#del fruit_tuple_2

#length of tuple
#print(len(fruit_tuple))

print(fruit_tuple)

#Sets
#A set is a collection which is unordered and unindexed. No duplicate members.
#A set is a mutable data structure - you can modify the elements in a set with methods like add and pop. A set is an unordered data structure, so you can't index and slice elements like a list; there is no sequence of positions to index with!

One of the key properties of a set is that it only contains unique elements. So even if you create a new set with a list of elements that contains duplicates, Python will remove the duplicates when creating the set automatically.
# create set
fruit_set = {'Apple', 'Orange', 'Mango'}

# check if in set
print('Apples' in fruit_set)

#add to set
fruit_set.add('Grape')

#remove from set
fruit_set.remove('Grape')

# clear set
#fruit_set.clear()
#del fruit_set

print(fruit_set)