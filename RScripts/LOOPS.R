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
for(i in 1:10) {
    print(i)
}
# for() is the function that will initialize the loop
# i is the iterative term
# 1:10 is a numeric vector from 1 to 10
# print(i) is the process

#################### Quick Exercise #############################
# a) You can add a mathematical operation to the previous process
for(i in 1:10) {
    print(i) # Add operation
}

# b) You can make the vector a character vector. See what happens
# Create a character vector
char_vector <- c("Alfredo", "Alejandro", "Ascanio", "Moreno") # Add character elements within "" to char_vector
for(i in char_vector) { # Substitute 1:10 for your character vector
    print(i)
}

#################### Practice with For-Loops ####################

#### a) Create a for-loop for printing elements from a character vector
char_vector <- LETTERS # You can change this vector if you want
# Option 1
for(char in char_vector) { 
    print(char)
}
# The iterative term doesn't need to be "i" always, it can be whatever you like
#Option 2
for(i in 1:length(char_vector)) {
    print(char_vector[i])
}


#### b) For-loop: mathematical operations on numeric vectors
math <- c(5, 8, 10, 13, 14, 17, 21, 24)
# Add 2 and print the output
for(i in math){
    #step 1
    #step 2
}

# Sum 2, divide by 3, raise to the power of the original number, and print
for(i in math){
    #step 1
    #step 2
    #step 3
    #step 4
}

#### c) For-loop by factor on a biological dataset
Data <- iris # Loading the data
head(iris) # Viewing part of the data

# Create a loop to extract the mean values of Sepal and Petal Length of each flower
for(___ in _____){
    # print the mean of Sepal.Length each species
}


###################################################################
####### Exercise 3: Let's sell drinks to multiple clients #########
###################################################################
source("Vending_Machine_Clients.R")
___ <- clients_line(100) # Save this into an object listing the 100 clients
Org_Drinks <- c(___, ___, ___) # Create a vector of original drinks
LacFree_Drinks <- c(___, ___, ___) # Create a vector of lactose-free drinks

for(_ in ____) {
    # Add and modify the conditional we created before accordingly
    #Print the status and drink given to each client
}


###################################################################
######## Exercise 4: Lets Join Data from different sources! #######
###################################################################

# You will use data from the species of manatee Trichechus manatus
# In the folder called Splitted_Tmanatus

# Example of joining two datasets
# Create a NULL Object
full_data <- NULL

# Read csv files
Data1 <- read.csv("Splitted_Tmanatus/Diveboard - Scuba diving citizen science.csv", stringsAsFactors = FALSE)
Data2 <- read.csv("Splitted_Tmanatus/Fort Fisher.csv", stringsAsFactors = FALSE)

# Joining two datasets by row (if they have the exact same columns' structure)
full_data <- rbind(Data1, Data2) 

# you can bind NULL objects with others, may be useful for your loop
full_data <- rbind(full_data, Data1, Data2) 

# list.files() allows you to list all the files in a folder
files <- list.files("Splitted_Tmanatus/")

# You can paste the folder name to your files
files <- paste("Splitted_Tmanatus/", files, sep = "")

#### Create your Loop ####


###################################################################
######################## While-Loops ##############################
###################################################################

#### Example of While loop ####
# Create X variable
x <- 1
# While-loop
while(x < 10) { # Condition within (), instead of sequence
    x = x + 1
    print(x)
}


####################### Quick Exercise ###########################

# Remember the coin_toss
coin_toss <- rbinom(n = 1, size = 1, prob = 0.5)
# Create X variable
x <- 1
# while-loop
while(x < 10) {
    # Add coin_toss
    # Add a conditional over the result of coin toss
    # In this case, there is no need to add an "else" statement, as nothing
    # should happen to x if we fail the coin_toss
    # Add a print of x
}

###################################################################
####################### Repeat-Loops ##############################
###################################################################

#### Example of repeat loop ####

# Create x variable
x <- 1
# Repeat-loop
repeat {
    x = x + 1
    print(x)
    if(x >= 10) {break()}
}
# We use the function break() after a conditional to stop the loop

####################### Quick Exercise ###########################

# Remember the coin_toss
coin_toss <- rbinom(n = 1, size = 1, prob = 0.5)
# Create X variable
x <- 1
# while-loop
repeat {
    # Add coin_toss
    # Add a conditional over the result of coin toss
    # In this case, there is no need to add an "else" statement, as nothing
    # should happen to x if we fail the coin_toss
    # Add a print of x
    # Add breaking condition
}

###################################################################