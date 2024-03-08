

#Define a function that counts the e's once the txt file is loaded
def count_the_es(name_of_file): #The function takes 1 kwarg, that is the name of the file to be checked
    with open(name_of_file, "r") as f: #Just open in read mode, no need to write this file
        read_file = f.read() #Pass a variable to the read in file

    counter = 0 #Initialise a counter at 0
    for character in read_file: #For each character in the file chosen...
        if character == "e": #If this character is an e, add 1 to he counter
            counter += 1
        else: # Otherwise, ignore it
            pass
    return counter #This function returns an integer that is the number of e's in the document

###### MAIN PROGRAM #########

import os
import sys

#Define a function that gets the name of the file from the command line
def how_many_es_in():#Takes no arguments
    args = sys.argv
    # Dealing with errors: want to concatenate filename with a space in it into 1 variable 
    # e.g. if the command line is $ es.py moby dick.txt
    # args[1:] = ["moby", "dick.txt"]
    # But filename variable should be "moby dick.txt"
    # Using .join with a whitespace ' ' between each element of the returned list 
    name_of_file = ' '.join(args[1:])
    
    #Ensure that the filename has a .txt extension
    if name_of_file[-4:] == ".txt": 
        #First, make sure the file exists and in saved to the working directory:
        if os.path.exists(name_of_file):
            print(f"{name_of_file} contains {count_the_es(name_of_file)} instances of the letter e.")  #If it does, carry out the count_the_es function defined earlier.
        else:
            print(f"Please save {name_of_file} to\n{os.getcwd()}\nin order to use this function.") #If not, prompt user to save the file to the correct location
    else:
        print("Please enter a .txt file.")

how_many_es_in()