#conditional statements 

#if statement : conditional statement that runs or skips code based on whether a condition is true or false
phone_balance = 10
bank_balance = 20
if phone_balance < 5: 
    phone_balance += 10
    bank_balance -= 10

print(bank_balance)

#use comparison operators in conditional statements
# == comparison not = (assignment operator)
if x == 5: 
    print("Hello World!")
# != 
if x != 5: 
    print("No World!")


#if, elif, else

#if must always start with if clause
if season == 'spring':
    print('plant the garden!')
#elif short for "else if" check for an addtional condition if condition in previous clauses in the if statement evaluate to false
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
#else must come at the end of an if statement. does not require a condition. will run if all other conditionals above are false
else:
    print('unrecognized season')




