#building dictionaries

# two important concepts: for loops and dictionary get method

#using a for loop to create a set of counters

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {}

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1 
    else:
        word_counter[word] += 1

#for loop iterates through each element in the list.
#first iteration word takes the value 'great'
#if statement checks if 'word' is in the 'word_counter' dicitonary
#