def personal_info(): #Exercise 1
    #personal info accepts no arguments
    #it collects the name, address, phone# and college major
    #it displays name, address, phone# and college major
    
    
    #Get the name
    name = input('Enter your name: ')
    
    #Get the address
    street_address = input('Enter your street address: ')
    citystate = input ('Enter your city and state: ')
    Zip = input('Enter your ZIP code: ')
    
    #Get telephone number
    t_number = input('Enter your telephone number: ')
    
    #Get the projected major
    college_major = input('Enter your projected college major: ')
    
    #Display the collected data
    print('Here is the data you entered:')
    
    print(name)
    print(street_address, citystate, Zip)
    print(t_number)
    print(college_major)
    
def total_purchase(): #Exercise 4
    #total purchase accepts no arguments
    #it collects the price for each item
    #it displays the subtotal, tax, and total price
    
    #Get the price for each item
    item1 = float(input('Please enter a price for your first item: '))
    item2 = float(input('Please enter a price for your second item: '))
    item3 = float(input('Please enter a price for your third item: '))
    item4 = float(input('Please enter a price for your fourth item: '))
    item5 = float(input('Please enter a price for your fifth item: '))
    
    #Find the Subtotal
    subtotal = item1 + item2 + item3 + item4 + item5
    
    #Calculate the tax
    TAX_RATE = 0.07
    tax = subtotal * TAX_RATE
    
    #Add to find the total
    total = subtotal + tax
    
    #Print the entire transaction with formatting
    print('Subtotal:  ', '$  ', format(subtotal, '4.2f'))
    print('Tax:       ', '$   ', format(tax, '4.2f'))
    print('Total:     ', '$  ', format(total, '4.2f'))
    
def distance_traveled(): #Exercise 5
    #distance traveled accepts no arguments
    #it collects the miles per hour
    #it displays the miles traveled in 6, 10, and 15 hours
    
    #Get the miles per hour of driving
    speed = int(input('How fast are you driving?'))
    
    #Calculate the distance for different times
    HOURS_6_AMOUNT = 6
    HOURS_10_AMOUNT = 10
    HOURS_15_AMOUNT = 15
    
    hours_6 = speed * HOURS_6_AMOUNT
    hours_10 = speed * HOURS_10_AMOUNT
    hours_15 = speed * HOURS_15_AMOUNT
    
    #Display the values calculated
    print('At', speed, 'miles per hour you will travel', hours_6, 'miles in 6 hours.')
    print('At', speed, 'miles per hour you will travel', hours_10, 'miles in 10 hours.')
    print('At', speed, 'miles per hour you will travel', hours_15, 'miles in 15 hours.')
    
def sales_tax(): #Exercise 6
    #sales tax accepts no arguments
    #it collects the sale amount of the purchase
    #it displays the purchase price, state tax, county tax, total tax, and total sale
    
    #Get the sale amount
    sale_amount = float(input('Enter the sale amount: '))
    
    #Calculate the state tax, county tax, total tax, and total sale price
    STATE_TAX_AMOUNT = 0.05
    COUNTY_TAX_AMOUNT = 0.025
    
    state_tax = sale_amount * STATE_TAX_AMOUNT
    county_tax = sale_amount * COUNTY_TAX_AMOUNT
    total_tax = state_tax + county_tax
    total_sale = total_tax + sale_amount
    
    #Print the amount of each value in dollar amount
    print('Your purchase price was:     $   ', format(total_sale, '5.2f'))
    print('Your state tax amount is:    $   ', format(state_tax, '5.2f'))
    print('Your county tax amount is:   $   ', format(county_tax, '5.2f'))
    print('Your total tax is:           $   ', format(total_tax, '5.2f'))
    print('Your total sale is:          $   ', format(total_sale, '5.2f'))
    
def tip_tax_total(): #Exercise 8
    #tip tax total accepts no arguments
    #it collects the sale amount of the purchase
    #It displays the tip amount, sales tax, and total bill
    
    #Use named constants for tip amount and sales tax
    TIP = .18
    SALES_TAX = 0.07
    
    #Get the sale amount
    sale_amount = float(input('Please enter the sale amount: '))
    
    #Calculate the tip amount, sales tax, and total bill
    tip_amount = sale_amount * TIP
    sales_tax = sale_amount * SALES_TAX
    total_bill = sale_amount + tip_amount + sales_tax
    
    #Display the calculated data
    print('The sale was:\t\t', '$', format(sale_amount, '6.2f'))
    print('The tip amount is:\t', '$', format(tip_amount, '6.2f'))
    print('The sales tax amount is:', '$', format(sales_tax, '6.2f'))
    print('The total bill is:\t', '$', format(total_bill, '6.2f'))
    
def temp_converter(): #Exercise 9
    #temp converter accepts no arguments
    #it collects the degrees in celcius
    #it displays the degress in fahrenheit
    
    #Set the constant change of celcius to fahrenheit as 9/5
    PROPORTION_CHANGE = 9/5
    
    #Collect the degrees in celcius
    celcius = float(input('Please enter the degrees Celcius: '))
    
    #Calculate the conversion from celcius to fahrenheit
    fahrenheit = PROPORTION_CHANGE * celcius + 32
    
    #Display the collected and found values
    print(celcius, 'degrees celcius is', fahrenheit, 'degrees fahrenheit.')
    
def cookie_monster(): #Exercise 10
    #cookie monster accepts no arguments
    #it collects the number of desired cookies
    #it displays the needed amounts of ingredients
    
    #Set the constants for ingredient amounts for the recipe
    #1.5 cups sugar, 1 cup butter, and 2.75 cups flour
    REC_SUGAR = 12
    REC_BUTTER = 8
    REC_FLOUR = 22
    
    #Set the constants for needed ingredient amounts per cookie
    #Divide the recipe amount by 24, as it makes 24 cookies
    SINGLE_SUGAR = REC_SUGAR / 24
    SINGLE_BUTTER = REC_BUTTER / 24
    SINGLE_FLOUR = REC_FLOUR / 24
    
    #Collect the desired amount of cookies
    desired = float(input('How many cookies do you want to make?'))
    
    #Calculate the needed amounts of ingredients for the desired amount of cookies
    need_sugar = SINGLE_SUGAR * desired
    need_butter = SINGLE_BUTTER * desired
    need_flour = SINGLE_FLOUR * desired
    
    #Calculate the integer and remainder values of the ingredients
    int_sugar = need_sugar // 8
    rem_sugar = need_sugar % 8
    int_butter = need_butter // 8
    rem_butter = need_butter % 8
    int_flour = need_flour // 8
    rem_flour = need_flour % 8
    
    #Display the required amounts of the ingredients for the desired cookies
    print('For', desired, 'cookies you will need:')
    print(int_sugar, 'cup(s)', rem_sugar, 'ounces of sugar.')
    print(int_butter, 'cup(s)', rem_butter, 'ounces of butter.')
    print(int_flour, 'cup(s)', rem_flour, 'ounces of flour.')
    
def class_demographics(): #Exercise 11
    #class demographics accepts no arguments
    #It collects the number of males and females
    #it displays the percentage composition of the class
    
    #Get the number of males and females in the class
    females = int(input('Enter the number of females:'))
    males = int(input('Enter the number of males:'))
    
    #Calculate the total number of people in class
    total = females + males
    
    #Calculate the percentage of males and females in the class
    per_females = females / total
    per_males = males / total
    
    #Display the calculated values
    print('The class consists of', format(per_females, '.0%'), 'females and', format(per_males, '.0%'), 'males.')
    
def tortuga_1(): #Exercise 15 pt 1
    #tortuga 1 accepts no arguments
    #it draws a compass
    
    import turtle
    
    #Setup the turtle
    turtle.setup(400, 400)
    turtle.penup()
    turtle.hideturtle()
    
    #Set constants for each edge of the compass
    WEST_X = -140
    WEST_Y = 0
    
    EAST_X = 140
    EAST_Y = 0
    
    NORTH_X = 0
    NORTH_Y = 140
    
    SOUTH_X = 0
    SOUTH_Y = -140
    
    NW_X = -70
    NW_Y = 70
    
    NE_X = 70
    NE_Y = 70
    
    SE_X = 70
    SE_Y = -70
    
    SW_X = -70
    SW_Y = -70
    
    #Set the thickness and draw the four lines of the compass
    turtle.goto(WEST_X, WEST_Y)
    turtle.pensize(3)
    turtle.pendown()
    turtle.goto(EAST_X, EAST_Y)
    turtle.penup()
    
    turtle.goto(NORTH_X, NORTH_Y)
    turtle.pendown()
    turtle.goto(SOUTH_X, SOUTH_Y)
    turtle.penup()
    
    turtle.goto(NW_X, NW_Y)
    turtle.pensize(2)
    turtle.pendown()
    turtle.goto(SE_X, SE_Y)
    turtle.penup()
    
    turtle.goto(SW_X, SW_Y)
    turtle.pendown()
    turtle.goto(NE_X, NE_Y)
    turtle.penup()
    
    #Write the Letters of each side of the compass
    
    turtle.goto(-10, 145)
    turtle.pendown()
    turtle.write('N', font=("Calibri", 25, "bold"))
    turtle.penup()
    
    turtle.goto(-5, -180)
    turtle.pendown()
    turtle.write('S', font=("Calibri", 25, "bold"))
    turtle.penup()
    
    turtle.goto(150, -20)
    turtle.pendown()
    turtle.write('E', font=("Calibri", 25, "bold"))
    turtle.penup()
    
    turtle.goto(-180, -20)
    turtle.pendown()
    turtle.write('W', font=("Calibri", 25, "bold"))
    turtle.penup()
    
def tortuga_2(): #Exercise 15 pt 2
    #tortuga 2 accepts no arguments
    #it draws a basic colored house
    
    import turtle
    
    #Set up the turtle
    turtle.setup(400, 450)
    turtle.penup()
    turtle.hideturtle()
    
    #set constants for each edge of the house
    
    ROOF_TOP_X = -50
    ROOF_TOP_Y = 150
    
    LEFT_TOP_X = -100
    LEFT_TOP_Y = 100
    
    RIGHT_TOP_X = 0
    RIGHT_TOP_Y = 100
    
    LEFT_B_X = -100
    LEFT_B_Y = 0
    
    RIGHT_B_X = 0
    RIGHT_B_Y = 0
    
    BACK_ROOF_X = 50
    BACK_ROOF_Y = 100
    
    BACK_TOP_X = 75
    BACK_TOP_Y = 75
    
    BACK_B_X = 75
    BACK_B_Y = 25
    
    #Draw the house outline
    #coloring the sections as they are finished
    
    turtle.fillcolor('grey')
    turtle.begin_fill()
    turtle.goto(LEFT_TOP_X, LEFT_TOP_Y)
    turtle.pendown()
    turtle.goto(ROOF_TOP_X, ROOF_TOP_Y)
    turtle.goto(RIGHT_TOP_X, RIGHT_TOP_Y)
    turtle.goto(LEFT_TOP_X, LEFT_TOP_Y)
    turtle.end_fill()
    
    turtle.fillcolor('brown')
    turtle.begin_fill()
    turtle.goto(LEFT_B_X, LEFT_B_Y)
    turtle.goto(RIGHT_B_X, RIGHT_B_Y)
    turtle.goto(RIGHT_TOP_X, RIGHT_TOP_Y)
    turtle.end_fill()
    
    turtle.begin_fill()
    turtle.goto(BACK_TOP_X, BACK_TOP_Y)
    turtle.goto(BACK_B_X, BACK_B_Y)
    turtle.goto(RIGHT_B_X, RIGHT_B_Y)
    turtle.end_fill()
    turtle.penup()
    
    turtle.goto(ROOF_TOP_X, ROOF_TOP_Y)
    turtle.pendown()
    
    turtle.fillcolor('grey')
    turtle.begin_fill()
    turtle.goto(BACK_ROOF_X, BACK_ROOF_Y)
    turtle.goto(BACK_TOP_X, BACK_TOP_Y)
    turtle.goto(RIGHT_TOP_X, RIGHT_TOP_Y)
    turtle.goto(ROOF_TOP_X, ROOF_TOP_Y)
    turtle.end_fill()
    