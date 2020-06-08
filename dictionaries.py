# a dictionary is a collection which is unordered, changeable and index no duplicate members
#A dictionary is a mutable, unordered data structure that contains mappings of keys to values. Because these keys are used to index values, they must be unique and immutable. For example, a string or tuple can be used as the key of a dictionary, but if you try to use a list as a key of a dictionary, you will get an error.
# simple dict

person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30
}

#constructor 
#person = dict(first_name = 'John', last_name = 'Doe', age = 30)

# access value
print(person['first_name'])
print(person.get('last_name'))

# add key/value
person['phone'] = '555-555-5555'

# get keys
print(person.keys())

# get values
print(person.items())

#make copy
person2 = person.copy()
person2['city'] = 'Boston'

# remove item
#del(person['age'])
person.pop('phone')

# clear 
person.clear()

# get length
print(len(person2))

print(person)


# list of dict

people = [
    {'name': 'Martha', 'age' : 40},
    {'name' : 'Bob', 'age' : 20}
]

print(people[1]['name'])


