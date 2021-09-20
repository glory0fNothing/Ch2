def comment_example():
    #comment example receives no arguments
    #It explains how to make a function header
    #and outputs or returns "Hello World!"
    print("Hello World!")

def program2_1(): #apostrophe output
    print('Kate Austen')
    print('123 Full Cirlce Drive')
    print('Asheville, NC 28899')
    
def program2_2(): #double quote output
    print("Kate Austen")
    print("123 Full Cirlce Drive")
    print("Asheville, NC 28899")
    
def program2_3(): #display apostrophe
    print("Don't fear!")
    print("I'm here!")
    
def program2_4(): #display quote
    print('Your assignment is to read "Hamlet" by tomorrow.')
    
def program2_5(): #comment 1
     #This function displays a person's name and address
    print('Kate Austen')
    print('123 Full Cirlce Drive')
    print('Asheville, NC 28899')
    
def program2_6(): #comment 1
    print('Kate Austen') #Display the name
    print('123 Full Cirlce Drive') #Display the address
    print('Asheville, NC 28899') #Display the city, state, and ZIP
    
def program2_7(): #variable demo 1
    #This program demonstrates a variable
    room = 503
    print('I am staying in room number')
    print(room)
    
def program2_8(): #variable demo 2
    #Create two variables: top_speed and distance
    top_speed = 160
    distance = 300
    
    #Display the values represented by the variables
    print('The top speed is')
    print(top_speed)
    print('The distance traveled is')
    print(distance)
    
def program2_9(): #vairable demo 3
    #This program demonstrates outputting a variable
    room = 503
    print('I am staying in room number', room)
    
def program2_10(): #variable demo 4
    #This program demonstrates a variable reassignment
    #Assign a value to the dollars variable
    dollars = 2.75
    print('I have', dollars, 'in my account.')
    
    #reassign dollars so it references a different value
    dollars = 99.95
    print('But now I have', dollars, 'in my account!')
    
def program2_11(): #string variable
    #Create variables to reference two strings
    
    first_name = "Kathryn"
    last_name = "Marino"
    
    #Display the values referenced by the variables
    print(first_name, last_name)
    
def program2_12(): #string input
    #Get the user's first name
    first_name = input('Enter your first name: ')
    
    #Get the user's last name
    last_name = input('Enter your last name: ')
    
    #Print a greeting to the user
    print('Hello', first_name, last_name)
    
def program2_13(): #input
    #Get the user's name, age, and income
    name = input('What is your name? ')
    age = int(input('What is your age? '))
    income = float(input('What is your income? '))
    
    print('Here is the data you entered:')
    print('Name:', name)
    print('Age:', age)
    print('Income:', income)
    
def program2_14(): #simple math
    #Assign a value to the salary variable
    salary = 2500.00
    
    #Assign a value to the bonus variable
    bonus = 1200.00
    
    #Calculate the total pay = salary + bonus
    pay = salary + bonus
    
    #Display the pay
    print('Your pay is', pay)
    
def program2_17(): #time converter
    #Get the number of seconds
    total_seconds = float(input('Enter the number of seconds: '))
    
    #Calculate the number of hours
    hours = total_seconds // 3600
    
    #Calculate the number of remaining minutes
    minutes = (total_seconds // 60) % 60
    
    #Calculate the number of remaining seconds
    seconds = total_seconds % 60
    
    #Output the results
    print('Here is the time in hours, minutes, and seconds:')
    print('Hours:', hours)
    print('Minutes:', minutes)
    print('Seconds:', seconds)
    
def program2_19(): #non formatted float
    #This program demonstrates how a floating point
    #number is displayed with no formatting
    
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    
    print('The monthly payment is', monthly_payment)
    
def program2_20(): #formatted float
    #This program demonstrates how a floating point
    #number can be formatted
    
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    
    print('The monthly payment is',
          format(monthly_payment, '.2f'))
    
def program2_21(): #currency display
    #This program demonstrates how a floating-point
    #number can be displayed as currency
    
    monthly_pay = 5000.00
    annual_pay = monthly_pay * 12
    
    print('Your annual pay is $',
          format(annual_pay, ',.2f'),
          sep='')

def program2_22(): #columns justified field width
    #This program displays the following
    #floating-point numbers into a column
    #with their decimal points aligned
    num1 = 127.8993
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999
    
    #Display each number in a justified field of 7 spaces
    #With two decimal spaces
    print(format(num1, '7.2f'))
    print(format(num2, '7.2f'))
    print(format(num3, '7.2f'))
    print(format(num4, '7.2f'))
    print(format(num5, '7.2f'))
    print(format(num6, '7.2f'))
    

    
