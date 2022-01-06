#this is a program to calculate the income tax of a person 
#all units are in dollars
#people having a income less that 30000$ have to pay 0 tax

print("Welcome")
print("Let's calculate your income tax")

#gross income
gross_income = float(input("What is your income : "))

if gross_income <= 30000:
    print("You are not eligible for income tax") 
    quit()
else:
    print("You are eligible for income tax")

#deductions
standard_deduction = 10000
dependents_deduction= 3000

print("You will have a standard deduction of 10000$")
no_of_dependents=int(input("How many dependent do u have :"))
print("You will have a deduction of 3000$ per dependent ")

taxable_income =gross_income -standard_deduction -(dependents_deduction*no_of_dependents)


print("Your taxable income is " + str(taxable_income)+"$")
rate= 20
tax= taxable_income*(rate/100)
print("Hence u will have to pay "+ str(tax) + "$ as tax")


