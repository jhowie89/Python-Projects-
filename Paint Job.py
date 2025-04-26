# For every 115sq ft = 1 gal , 8 hr
#labor = $20 per hr


sf = float(input("Enter the square feet "))
ppg = float(input("Price of paint per gallon "))

gal = sf / 115
hrs = gal * sf 
paint_cost = gal * ppg 
labor_cost = hrs * 20
total_cost = paint_cost * labor_cost 

print("The number of gallons of paint you need " , gal)
print("The hours of labor required " , hrs)
print("The cost of paint " ,paint_cost)
print("Labor charges are " , labor_cost)
print("Total cost of paint job " , total_cost)

