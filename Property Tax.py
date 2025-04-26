#Property Tax

#Get property value
#Calulate the assessment value by 60% of property value
#Calulate property tax asssessment/100 * .64 



property_value = float(input("Enter Property value"))
assessment_value= property_value * .64
tax = (assessment_value/100) * .64

print("Assessment Value" , assessment_value)
print("Property Tax" , tax)