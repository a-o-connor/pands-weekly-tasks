#bank.py
#Author: Ailsa O'Connor
#Week 02 Task: Create a program that does the following:
#Prompt the user and read in two money amounts (in cent)
#Add the two amounts
#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
#First, we need two integer inputs that will prompt "Enter amount1 (in cent)" and "Enter amount2 (in cent)"

#amount1=input("Enter first amount (in cents): ")
#amount2=input("Enter second amount (in cents): ")

#Edit: Need these to be integers so they're not read as strings. 
amount1=int(input("Enter first amount (in cents): "))
amount2=int(input("Enter second amount (in cents): "))

#create a line of code that adds the two input integers (want it in euro in the final output so divide by 100)
amount3= (amount1+amount2)/100

#Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount
#add f before the "" so that anything in {} reads in that variable and not verbatim 

#print(f"The sum of these is {amount3}")

#Read in  amount3 with 2 decimal places:
print(f"The sum of these is €{amount3:.2f}")
