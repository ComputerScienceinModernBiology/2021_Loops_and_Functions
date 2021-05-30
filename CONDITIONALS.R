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
coin_toss <- rbinom(n = 1, size = 1, prob = 0.5)
# Set condition for success, define process to occur if conditions
# are TRUE or FALSE and corresponding outputs
if(coin_toss == 1) { 
    print("You Win")
} else { 
    print("You Lose")
}


# What if we want the output to be Head or Tails, instead of winning or losing? 
# What if the coin is rigged, favoring heads over tails? 
# Change the code to make it happen

# Simulate a coin toss
coin_toss <- rbinom(n = 1, size = 1, prob = ___)
# Set condition for success, define process to occur if conditions
# are TRUE or FALSE and corresponding outputs
if(coin_toss == 1) { 
    print(______)
} else { 
    print(______)
}


###################################################################
########### Examples of Comparison/Logical Operators ##############
###################################################################

# You can change the values of X and Y if you want
x <- 5; y <- 8
x > y #is x greater than y? Results to FALSE
x < y #is x less than y? Results to TRUE
x >= y #is x equal to or greater than y? Results to FALSE
x <= y #is x equal to or less than y? Results to TRUE
x == y #is x equal to y? Results to FALSE
x != y #is x different to y? Results to TRUE
x %in% y #is the value of x contained in the values of y? Results FALSE

###################################################################
########### Examples of functions with logical outputs ############
###################################################################

# You can change the values of X and Y if you want
x <- c(F, F, F); y <- c(F, F, T)
identical(x, y) #if two objects are exactly the same returns one TRUE

any(x) #Input is a logical vector, if any value is TRUE, returns one TRUE
any(y) 

all(y) # input is a logical vector, if all values are TRUE, returns one TRUE

##### is.() #Family of functions
is.numeric(x) # if vector or matrix is numeric, returns TRUE
is.integer(y) # if vector or matrix is integer, returns TRUE
is.vector(x) # if object is vector, returns TRUE, etc…
is.logical(x)
#There are many more that you will discover as you start needing them

###################################################################
################## Exercise 2: Vending Machine ####################
###################################################################
source("Vending_Machine_Clients.R")

___ <- client_arrives() # Create a variable/vector representing the client
Org_Drinks <- c(___, ___, ___) # Create a vector of original drinks
LacFree_Drinks <- c(___, ___, ___) # Create a vector of lactose-free drinks


if() {
    #print client status regarding lactose intolerance
    #print a random drink from the appropriate selection
} else {
    #print client status regarding lactose intolerance
    #print a random drink from the appropriate selection
}
###################################################################
 