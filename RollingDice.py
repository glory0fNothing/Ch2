def rollingDice():
    #rolling Dice accepts no arguments
    #it gives a random value from 1 through 6
    #it prompts for another roll
    
    import random
    
    looping = True
    
    while looping == True:
        
        number = random.randint(1, 6)
    
        print(number)
        
        answer = input('Roll again?').lower()
    
        if answer == 'no':
            looping = False
            
rollingDice()