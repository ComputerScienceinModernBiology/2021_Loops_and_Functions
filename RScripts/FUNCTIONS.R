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

sample(x = c("A", "B", "c", "D"), size = 2) # select two random elements from X
sample(x = 1:20, size = 5) # Select 5 random elements from the vector of 1:20
sample(1:20, 5)            # Select 5 random elements from the vector of 1:20

# Help of sample
?sample
help(sample)

# Arguments of sample
args(sample)

# Code of sample()
sample # Shows in console
View(sample) # Shows in another script tab

###################################################################
############# Let's write our first function! #####################
###################################################################

# a) create a function that multiplies two numbers
Multiplication <- function(X, Y) { # Add arguments
    # Internal process
    Z = X*Y
    return(Z)
}

Multiplication(X = 3, Y = 8)
Multiplication(2, 9)
Multiplication()

# b) Add default values to our previous function
# X should default to 1, and Y to 7

Multiplication <- function(X = ___, Y = ____) { # Add default values
    # Internal process
    z = _____
    return(Z)
}

Multiplication()
Multiplication(Y = 8, X = 3)
Multiplication(9)

###################### Quick Exercise #############################

# Create a function called "power_of" that will raise one number "X"
# to the power of the second number "Y". Set default values in a way
# that, whenever the second number (Y) is not provided, the result of power_of(X)
# will be 1

power_of <- function(____, ____){
    #Internal process
}

power_of(2, 2) # Should result in 4
power_of(2, 0) # Should result in 1
power_of(3, 3) # Should result in 27
power_of(434)  # Should result in 1

###############################################################################
##### Exercise 5: Build a function to sell drinks to any number of clients ####
###############################################################################
source("Vending_Machine_Clients.R")

clients <- clients_line(1000)
sell_drinks <- function(Clients) {
    #Internal process - Loop and conditionals
    for(){
        if() { # FILL IN CONDITION WITHIN ()
               #FILL IN PROCESS 1
        } else {
               #FILL IN SECONDARY PROCESS
        }
    }
    
}

sell_drinks(Clients = clients) # Should print the list of clients conditions and random drink from selection, for any number of clients


