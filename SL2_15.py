def sale_price():
    #Get the original price of the item
    original_price = float(input("Enter the item's original price: "))
    
    #Calculate 20 percent of the original price.
    #This is the amount of the discount.
    discount = original_price * .20
    
    #Subtract the discount from the original price.
    #This is the sale price.
    sale_price = original_price - discount
    
    #Output the display price
    print('The sale price is', sale_price)
sale_price()