def future_value():
    #Get the desired value from the user
    desired = float(input('Enter the desired future value: '))
    
    #Get the annual interest rate
    interest_rate = float(input('Enter the annual interest rate: '))
    
    #Get the number of years that the money will accrue interest
    years = float(input('Enter the number of years the money will grow: '))
    
    #Calculate the amount that will need to be deposited
    deposit = desired /(1.0 + interest_rate)**years
    
    #Output the amount that will need to be deposited
    print('You will need to deposit $', format(deposit, '.2f'), sep='')
    
future_value()
