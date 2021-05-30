import numpy as np
# Function representing ONE client on the Vending Machine
def client_arrives():
    n, p, size = 1, .36, 1  # number of trials, probability of each trial
    status = np.random.binomial(n, p, 1)
    if(status == 1):
        person = "Lactose Intolerant"
    else:
        person = "Non-Lactose Intolerant"
    return person
#client_arrives()

# Function representing multiple clients on the Vending Machine
def clients_line(x = 10):
    clients = []
    client_list = range(1, x)
    for i in client_list:
        client = client_arrives()
        clients.append(client)
    return clients

#clients_line()
