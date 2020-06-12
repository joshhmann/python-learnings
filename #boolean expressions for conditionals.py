#boolean expressions for conditionals

#complex boolean expressions examples
#may contain multiple comparisons operators, logical operators, and even calculations
if 18.5 <= weight / height**2 < 25: 
    print("BMI is considered 'normal")

if is_raining and is_sunny: 
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location "CAN"):
    print("send email")

#and or and not
#however simple or complex, the condition in an if statement must be a boolean expressions that 
#evaluates either True or False and it is this value that decides whether the inded block in an if
#statement executes or not

#don't use True or False as conditions
if True: 
    print("This indented code will always get run.")


if False: 
    print("statement following this if statement would never be executed")


#another bad example
if is_cold or not is_cold:
    print("This indented code will always get run")

#be careful writing expressions that use logical operators
if weather == "snow" or "rain":
    print("wear boots!")

#don't compare a boolean variable with == True or == False
if is_cold == True:
    print("The weather is cold!")

#more readable code
if is_cold:
    print("The weather is cold!")

#if you want to check whether a boolean is False, use not operator

#truth value testing
#if using a non-boolean object as a condition in an if statement in place ofthe boolean expression
#python will check for truth value and use that to decide whether or not to run the indented code
#trueth value of an object in Python is considered True unless specified as False in the doc

#built-in objects that are False in Python
#constants defined to be false: None and False 
#zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

#errors has the truth value True because it's a non-zero number so error message is printed. 
errors = 3 
if errors: 
    print("You have {} errors to fix!".format(errors))
else: 
    print("No errors to fix!")





