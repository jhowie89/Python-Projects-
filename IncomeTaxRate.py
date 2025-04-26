def compute_Tax(income):
    Tax = 0
    if income > 30000:
        Tax = income  * 0.255 
         
    elif income > 20000:
        Tax = income* 0.15
        
    elif income > 10000:
        Tax = income* 0.105
        
    elif income > 5000:
        Tax = income * 0.5
        
    else:
        tax = income * 0
    return round(Tax)


income = int(input("Enter Income: $" ))
if income < 0:
    print("Error: Income can not be negative. Please enter valid positive amount. ")
else:
    tax_owed = compute_Tax(income) 
    print("taxed owed $ ", tax_owed)
