def get_average():
    #Get the first test score
    score_1 = float(input('Enter the first test score: '))
    
    #Get the second test score
    score_2 = float(input('Enter the second test score: '))
    
    #Get the third test score
    score_3 = float(input('Enter the third test score: '))
    
    #Calculate the average
    average = (score_1 + score_2 + score_3) / float(3)
    
    #Output the average
    print('The average score is:', average)
    
get_average()