#Auto Cost

loan_payment = float(input("How much is your loan payment $ " ))
ins = float(input("How much is your insurance $ "))
gas = float(input("What is your estimated fuel use $"))
oil = float(input("Estimated amount of oil $"))
tires = float(input("How much are your tires $"))
main = float(input("Estimated maintentenance cost $"))

total_monthly = loan_payment + ins + gas + oil + tires + main
total_yearly = total_monthly * 12

print("Your monthly amount is" , total_monthly)
print("your yearly amount is" , total_yearly)