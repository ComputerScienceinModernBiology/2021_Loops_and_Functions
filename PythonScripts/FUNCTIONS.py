#### Computer Science Workshop
#### Miami University
#### Course: Loops and Functions in R
#### Instructor: Alfredo Ascanio
#### Assistant instructors: Luis M. Montilla, Hank Stevens
#### Date: 08/02/2021-08/06/2021

###################################################################
######################### Functions ###############################
###################################################################

############## Example of a function: sample() ###################
from random import sample

sample(population = ["A", "B", "C", "D"], k = 2) # select two random elements from X
sample(population = range(1, 20), k = 5) # Select 5 random elements from the vector of 1:20
sample(k = 5, population = range(1, 20)) # Select 5 random elements from the vector of 1:20
sample(range(1, 20), 5) # Select 5 random elements from the vector of 1:20

# Help of sample
help(sample)

# Arguments of sample
import inspect
inspect.signature(sample)

# Code of sample()
print(inspect.getsource(sample)) # Shows in console

###################################################################
############# Let's write our first function! #####################
###################################################################

# a) create a function that multiplies two numbers
def Multiplication(X, Y): # Add arguments
    # Internal process
    Z = X*Y
    return(Z)


Multiplication(X = 3, Y = 8)
Multiplication(2, 9)
Multiplication()

# b) Add default values to our previous function
# X should default to 1, and Y to 7

def Multiplication(X _____, Y _____): # Add default values
    # Internal process
    Z = X*Y
    return(Z)


Multiplication()
Multiplication(Y = 8, X = 3)
Multiplication(9)

###################### Quick Exercise #############################

# Create a function called "power_of" that will raise one number "X"
# to the power of the second number "Y". Set default values in a way
# that, whenever the second number (Y) is not provided, the result of power_of(X)
# will be 1

def power_of(X = ___, Y = ___):
    _____ #Internal process


power_of(2, 2) # Should result in 4
power_of(2, 0) # Should result in 1
power_of(3, 3) # Should result in 27
power_of(434)  # Should result in 1

###############################################################################
##### Exercise 5: Build a function to sell drinks to any number of clients ####
###############################################################################
from Vending_Machine_Clients import *

clients = clients_line(1000)
def sell_drinks(Clients):
    # Internal process - Loop and conditionals
    for ___ in __:
        if _____:  # FILL IN CONDITION WITHIN ()
        # FILL IN PROCESS 1
        else:
        # FILL IN SECONDARY PROCESS

sell_drinks(Clients=clients)  # Should print the list of clients conditions and random drink from selection, for any number of clients


