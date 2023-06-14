#This program is a calculator that can calculate either simple or compond interest on investments 
#It can also calculate the amount of interest you will pay on a home loan

#Line of code that the compulsary task told us to include at the start of the program
import math


#Introducing the functions of the finance calculator to the user
print("\nHello and welcome to the finance calculator\n\nThis program will give you access to an investment calculator and a home loan repayments calculator.")
print("\nInvestment - to calculate the amount of interest you'll earn on your investment\nBond - to calculate the amount you'll have to pay on a home loan")


#Setting the variable for the choice of calculator made by the user and displaying this 
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
choice = choice.lower()



#First if statement to take the user to the investment calulator.
if choice == "investment": 
    print("\nYou have chosen the {} calculator.\n".format(choice))
    deposit_value = int(input("Please enter the amount of money you are depositing e.g. 10000:")) #All of the values for the calculation cast as integers
    interest_rate = int(input("Please enter the interest rate e.g. enter 5 percent as 5: "))
    interest_rate_pecentage = float(interest_rate/100)
    interest_years = int(input("Please enter the number of years you plan on investing for e.g. 3: "))
    interest = True
    interest_choice = (input("Would you like 'simple' or 'compound' interest? Enter 1 for 'simple' and 2 for 'compound'."))

    if interest_choice == "1": #Nested if statement to run either the simple or compound calculation
        interest = True
        simple_interest = deposit_value * (1 + interest_rate_pecentage*interest_years)
        rounded_simple_interest = float(round(simple_interest, 2))     
        print("\nYour total investment with simple interest = £{}".format(rounded_simple_interest))
    else:
        interest = False
        compound_interest = deposit_value * math.pow((1+interest_rate_pecentage),interest_years)
        rounded_compound_interest = float(round(compound_interest, 2))    
        #I used an explanation from the 'free code camp' website to get the syntax round(number, decimal_point)
        print("\nYour total investment with compound interest = £{}".format(rounded_compound_interest))


#elif statement used to display bond calculator. or has been used again to allow user to input choice in upper or lower case
elif choice == "bond":
    print("\nYou have chosen the {} calculator.\n".format(choice))
    present_house_value = int(input("Please enter the present value of your house e.g. 1000000: "))
    bond_interest_rate = int(input("Please enter the interest rate e.g. enter 7 percent as 7: "))
    bond_interest_rate_monthly = bond_interest_rate / 12
    bond_interest_rate_monthly_percentage = float(bond_interest_rate_monthly/100)
    repayment_months = int(input("Please enter the number of months over which you plan to repay the bond e.g. 120: "))
    monthly_repayment_value = (bond_interest_rate_monthly_percentage * present_house_value) / (1 - ((1 + bond_interest_rate_monthly_percentage)**-repayment_months))
    rounded_monthly_repayment_value = round(monthly_repayment_value, 2)
    print("\nYour monthly repayment value is: £{}".format(rounded_monthly_repayment_value))
   


#Using an else statement to direct to the error message if a valid choice has not been made
else:
    print("\nError: You have not entered a valid input") 