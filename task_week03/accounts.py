# Weekly Task 03: 
# Program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs)
# Author: A OConnor


# Input to read in the 10 digit account number
# Want to only accept numbers here so use int()
# accountno = int(input("Please enter an 10 digit account number: "))
# # Now it will be required to be a string so that it can be spliced
# accountno_asstring = str(accountno)
# #Splice the 10 digit account number into the last 4 digits
# #From W3 schools: Strings are arrays, and square brackets can be used to access elements of the string
# #Can index the last 4 elements of a 10 element string through slicing
# #Python indexing starts on 0, need to index from [6:9] (or [6: ] will slice to the end)
# last4digits = accountnostring[6:]
# print(f"xxxxxx{last4digits}")


#Extra: Modify the program to deal with account numbers of any length
#Assuming the user inputs a 12 digit number: want the output to read 8 x's and 4567
# Input to read in the account number
#Again, want to only accept numbers here so use int()
accountno = int(input("Please enter your account number: "))
#Again, convert to a string so it can be more easily manipulated: 
accountno_asstring = str(accountno)
#W3 schools: To get the length of a string, use the len() function
accountno_length = len(accountno_asstring)
#Use the accountno_length integer to index the account number
#Subtracting 4 from the length of the account number will give the correct number of x's to write and the index to slice the string!
accountno_length_minus4 = int(accountno_length - 4)
##print(accountno_asstring [accountno_length_minus4:])
#To get Python to print x accountno_length_minus4 times
##print("x" *accountno_length_minus4)
#Concetenate! Ensure to convert back into string the last 4 digits so that can be concantenates
print("x" *accountno_length_minus4 + str(accountno_asstring [accountno_length_minus4:]))