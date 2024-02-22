#A program that takes an integer input and performs a collatz sequence on that integer
#Continue the sequence until the value is 1
#Author: A. O'Connor

#Initialize the variable: Ask user to input an integer.
yournumber = int(input("Please enter a positive integer: "))

#Initialize an empty list to append each new variable to and print when 1 has been reached
numbers = []

#Check if the number is 1:
while yournumber != 1:
    #While the number is not equal to 1, do something to it:
    if yournumber%2 == 0:           #If the number is even, divide by 2   
        yournumber = yournumber/2   #Update the variable
        numbers.append(yournumber)  #Add it to the list
    else:                               #If the numbber is odd, multiply by 3 and add 1
        yournumber = (yournumber*3)+1   #Update the variable
        numbers.append(yournumber)      #Add it to the list 
print("This sequence has reached 1")

#Print the list 
print(numbers)


#Just for fun, lets plot this hailstone sequence
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.plot(numbers)
plt.show()







    

