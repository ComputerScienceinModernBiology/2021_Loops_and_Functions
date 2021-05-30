#### Computer Science Workshop
#### Miami University
#### Course: Loops and Functions in R
#### Instructor: Alfredo Ascanio
#### Assistant instructors: Luis M. Montilla, Hank Stevens
#### Date: 08/02/2021-08/06/2021

###################################################################
######################### For-Loops ###############################
###################################################################

# Structure of a for loop #
for i in range(1, 10):
    print(i)

# for is the function that will initialize the loop
# i is the iterative term
# range(1, 10) is a list of numbers from 1 to 10
# print(i) is the process

#################### Quick Exercise #############################
# a) You can add a mathematical operation to the previous process
for i in range(1, 10):
    print(i) # Add operation

# b) You can make the list a list of strings. See what happens
# Create a character list

char_vector = ["Alfredo", "Alejandro", "Ascanio", "Moreno"] # Add character elements within "" to char_vector
for i in char_vector: # Substitute 1:10 for your character vector
    print(i)

#################### Practice with For-Loops ####################

#### a) Create a for-loop for printing elements from a character vector
from string import ascii_lowercase
char_vector = ascii_lowercase # You can change this vector if you want
# Option 1
for char in char_vector:
    print(char)

# The iterative term doesn't need to be "i" always, it can be whatever you like

#Option 2
for i in range(0, len(char_vector)):
    print(char_vector[i])



#### b) For-loop: mathematical operations on numeric vectors
math = [5, 8, 10, 13, 14, 17, 21, 24]
# Add 2 and print the output
for i in math:
    z = #Add process
    print(z)


# Add 2, divide by 3, raise to the power of the original number, and print
for i in math:
    z = #Add step 1
    z = #Add step 2
    z = #Add step 3
    print(z)


#### c) For-loop by factor on a biological dataset
#pip install -U pandas
import pandas as pd
from statistics import mean

Data = pd.read_csv("iris_csv.csv")
Data
Data.head() # Viewing part of the data
# Create a loop to extract the mean values of Sepal and Petal Length of each flower
for i in Data.Species.unique():
    print(mean(Data[Data['Species'] == i].sepallength))


###################################################################
####### Exercise 3: Let's sell drinks to multiple clients #########
###################################################################
from Vending_Machine_Clients import *
___ = clients_line(100) # Save this into an object listing the 100 clients
Org_Drinks = [___, ___, ___] # Create a vector of original drinks
LacFree_Drinks = [___, ___, ___] # Create a vector of lactose-free drinks

for ___ in ____:
    # Add and modify the conditional we created before accordingly
    #Print the status and drink given to each client


###################################################################
######## Exercise 4: Lets Join Data from different sources! #######
###################################################################

# You will use data from the species of manatee Trichechus manatus
# In the folder called Splitted_Tmanatus

# Example of joining two datasets
# Create a NULL Object
from os import listdir

full_data = pd.DataFrame()

# Read csv files
Data1 = pd.read_csv("Splitted_Tmanatus/Diveboard - Scuba diving citizen science.csv")
Data2 = pd.read_csv("Splitted_Tmanatus/Fort Fisher.csv")

# you can append NULL objects with others, may be useful for your loop
full_data = full_data.append(Data1, ignore_index = True)

# Joining two datasets by row (if they have the exact same columns' structure)
full_data = pd.concat([Data1, Data2])

from os import listdir
# listdir() allows you to list all the files in a folder
files = listdir("Splitted_Tmanatus")

# You can paste the folder name to your files
for i in range(0, len(files)):
    files[i] = "Splitted_Tmanatus\\" + files[i]
files

#### Create your Loop ####
full_data = pd.DataFrame()
for i in range(0, len(files)):
    Data = pd.read_csv(files[i])
    Data = Data[Data["year"] > 1970]
    full_data = full_data.append(Data, ignore_index = True)


###################################################################
######################## While-Loops ##############################
###################################################################

#### Example of While loop ####
# Create X variable
x = 1
# While-loop
while x < 10:  # Condition within (), instead of sequence
    x = x + 1
    print(x)



####################### Quick Exercise ###########################

# Remember the coin_toss
import numpy as np

n, p, size = 1, .5, 1  # number of trials, probability of each trial
coin_toss = np.random.binomial(n, p, 1)

# Create X variable
x = 1
# while-loop
while x < 10:
    # Add coin_toss
    if _____: # Add a conditional over the result of coin toss
        _____# In this case, there is no need to add an "else" statement, as nothing
        _____# should happen to x if we fail the coin_toss
        _____# Add a print of x

###################################################################
####################### Repeat-Loops ##############################
###################################################################

#### Example of repeat loop ####

# Create x variable
x = 1
# Repeat-loop in python can be created as a modification of while-loop
while True:
    x = x + 1
    print(x)
    if x >= 10:
        break

# We use the function break after a conditional to stop the loop

####################### Quick Exercise ###########################

# Remember the coin_toss
n, p, size = 1, .5, 1  # number of trials, probability of each trial
coin_toss = np.random.binomial(n, p, 1)
# Create X variable
x = 1
# while-loop
while True:
    coin_toss = np.random.binomial(n, p, 1) # Add coin_toss
    if coin_toss == 1: # Add a conditional over the result of coin toss
        x = x + 1
        ____ # In this case, there is no need to add an "else" statement, as nothing
        ____ # should happen to x if we fail the coin_toss
        ____ # Add a print of x
        ____ # Add breaking condition

###################################################################