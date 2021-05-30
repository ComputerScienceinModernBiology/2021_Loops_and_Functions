# Function representing ONE client on the Vending Machine
client_arrives <- function() {
    if(rbinom(1, size = 1, prob = 0.36) == 1) {
        person <- "Lactose Intolerant"
    } else {
        person <- "Non-Lactose Intolerant"
    }
    person
}


# Function representing multiple clients on the Vending Machine
clients_line <- function(x = 10) {
    clients <- NULL
    for(i in 1:x) {
        clients[i] <- client_arrives()
    }
    clients
}
