# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("The insurance cost for female and non-smoker with 3 children is " + str(insurance_cost) + " dollars.")

# Age Factor
age = 32
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("The new insurance cost is " + str(new_insurance_cost) + " dollars.")
change_in_insurance_cost = abs(new_insurance_cost - insurance_cost)
print("The change in estimated insurance cost after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars")

# BMI Factor
age = 28
bmi+= 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("The new insurance cost is " + str(new_insurance_cost) + " dollars.")
change_in_insurance_cost = abs(new_insurance_cost - insurance_cost)
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars")
# Male vs. Female Factor
sex = 1
bmi= 26.2
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("The new insurance cost is " + str(new_insurance_cost) + " dollars.")
change_in_insurance_cost = abs(new_insurance_cost - insurance_cost)
print("The change in estimated insurance cost for male is " + str(change_in_insurance_cost) + " dollars")

# smoker vs non-smoker
sex = 0
smoker = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("The new insurance cost is " + str(new_insurance_cost) + " dollars.")
change_in_insurance_cost = abs(new_insurance_cost - insurance_cost)
print("The change in estimated insurance cost for female and if she is a smoker " + str(change_in_insurance_cost) + " dollars")
# number of children 
smoker = 0
number_of_children = 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("The new insurance cost is " + str(new_insurance_cost) + " dollars.")
change_in_insurance_cost = abs(new_insurance_cost - insurance_cost)
print("The change in estimated insurance cost for female and with increased in number children " + str(change_in_insurance_cost) + " dollars")
#person is over 70 years
number_of_children = 3
age = 70
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("The new insurance cost is " + str(new_insurance_cost) + " dollars.")
change_in_insurance_cost = abs(new_insurance_cost - insurance_cost)
print("The change in estimated insurance cost for female with the age of 70 years is " + str(change_in_insurance_cost) + " dollars")

print ( "BMI, smoker and age indeed plays important role in change of insurance cost. But female has to pay higher insurance cost in comparision to male for all same charcterstics.")
