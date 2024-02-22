#bank.py
#Author: Ailsa O'Connor
#Week 02 Task: Create a program that does the following:
#Prompt the user and read in two money amounts (in cent)
#Add the two amounts
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#First, we need two integer inputs that will prompt "Enter amount1 (in cent)" and "Enter amount2 (in cent)"
#amount1=input("Enter first amount (in cents): ")
#amount2=input("Enter second amount (in cents): ")
#well that's no good, we need these to be integers so they're not read as strings. 
#gonna try using column selection mode to edit the two lines at once, we'll see if this works
amount1=int(input("Enter first amount (in cents): "))
amount2=int(input("Enter second amount (in cents): "))
#it worked!
#create a line of code that adds the two input integers (want it in euro in the fical output so /100)
amount3= (amount1+amount2)/100
#just putting a print here, i'll comment it out later, to check if that works
#print(amount3)
#wooohoo it works
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
#add f before the "" so that anythig in {} reads in that variable and not verbatim 
#print(f"The sum of these is {amount3}")
#that works but
#read in  amount3 with 2 decimal places
#print(f"The sum of these is {amount3:.2f}")
#And add a euro symbol
print(f"The sum of these is €{amount3:.2f}")