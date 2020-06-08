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



