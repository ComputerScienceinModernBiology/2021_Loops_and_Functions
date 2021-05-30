#### Computer Science Workshop
#### Miami University
#### Course: Loops and Functions in R
#### Instructor: Alfredo Ascanio
#### Assistant instructors: Luis M. Montilla, Hank Stevens
#### Date: 08/02/2021-08/06/2021

###################################################################
################### Conditionals ##################################
###################################################################

###################################################################
################### Exercise 1: Coin Toss Game ####################
###################################################################

# Coin Toss Example
# Simulate a coin toss
import numpy as np
n, p, size = 1, .5, 1  # number of trials, probability of each trial
coin_toss = np.random.binomial(n, p, 1)
# Set condition for success, define process to occur if conditions
# are TRUE or FALSE and corresponding outputs
if coin_toss == 1:
    print("You Win")
else:
    print("You Lose")

# What if we want the output to be Head or Tails, instead of winning or losing?
# What if the coin is rigged, favoring heads over tails?
# Change the code to make it happen

# Simulate a coin toss
n, p, size = 1, ___, 1  # number of coin tosses, probability of success,
coin_toss = np.random.binomial(n, p, 1)
# Set condition for success, define process to occur if conditions
# are TRUE or FALSE and corresponding outputs
if coin_toss == 1:
    print("____")
else:
    print("____")

###################################################################
########### Examples of Comparison/Logical Operators ##############
###################################################################

# You can change the values of X and Y if you want
x, y = 5, 8
print(x > y)  # is x greater than y? Results to FALSE
print(x < y)  # is x less than y? Results to TRUE
print(x >= y)  # is x equal to or greater than y? Results to FALSE
print(x <= y)  # is x equal to or less than y? Results to TRUE
print(x == y)  # is x equal to y? Results to FALSE
print(x != y)  # is x different to y? Results to TRUE
y = [5, 9]
print(x in y)  # is the value of x contained in the values of y? Results FALSE

###################################################################
########### Examples of functions with logical outputs ############
###################################################################

# You can change the values of X and Y if you want
x = [False, False, False];
y = [False, False, True]
print(x == y)  # if two objects are exactly the same returns one TRUE

print(any(x))  # Input is a logical vector, if any value is TRUE, returns one TRUE
print(any(y))

print(all(y))  # input is a logical vector, if all values are TRUE, returns one TRUE

# As objects in python are different, the usage of the is. family of functions is also different

###################################################################
################## Exercise 2: Vending Machine ####################
###################################################################
source("Vending_Machine_Clients.R")

___ = client_arrives() # Create a variable/vector representing the client
Org_Drinks = [___, ___, ___] # Create a vector of original drinks
LacFree_Drinks = [___, ___, ___] # Create a vector of lactose-free drinks

if ____ :
    #print client status regarding lactose intolerance
    #print a random drink from the appropriate selection
else ____ :
    #print client status regarding lactose intolerance
    #print a random drink from the appropriate selection

###################################################################
