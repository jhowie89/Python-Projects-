#Stadium Seating 

class_a = float(input("Enter Class A ticket sales "))
class_b = float(input("Enter Class B ticket saales "))
class_c = float(input("Enter Class C tickets sales "))

total_sales = (class_a * 15) + (class_b * 12) + (class_c * 9)
print("The total ticket sales is " , total_sales)