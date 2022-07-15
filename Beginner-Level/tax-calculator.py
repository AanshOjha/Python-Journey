income = float(input("Please enter your Annual Income - "))

if income < 85528 and income > 0 :
    tax = 0.18 * income - 556.2
    round(tax)
    print("The tax is: , " + str(tax) + "Thalers")

elif income < 0 :
    print("Please do not put negativity :)")

elif income == 0 :
    print("Please earn some money before paying tax 😁")

elif income > 85528 :
    tax2 = 14839.2 + (0.32 * (income - 85528))
    round(tax2)
    print("The tax is: " + str(tax2) + "Thalers")
