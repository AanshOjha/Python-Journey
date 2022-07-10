#converts US Dollar to Indian Rupees

amount = int(input('HI ! I CONVERT US DOLLAR TO INR, CREATED BY AANSH OJHA !\nPLEASE ENTER THE AMOUNT YOU WANT TO CONVERT TO INR.\n'))
answer = amount * float(79.26)
if (amount < 0): 
    print('What are you doing, could you please enter a Positive value...\n')

else :
    print('OK !' + ' ' + str(amount) + ' ' + 'Dollars is equal to' + ' ' + str(answer) + ' ' + 'Rupees')

