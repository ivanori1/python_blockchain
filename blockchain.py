# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Return the last value of the current bolckchain"""
    return blockchain[-1]

# This function accepts two arguments,
# One requred one(transaction_amount) and the optional (last_transaction)
# Last ransaction is optional because it have default [1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as also the last transaction to blockchain
    Arguments:
        :transaction_amount: the amount to set by user input
        :last_transaction: the last blockchain transaction (default [1])
     """
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


def get_user_input():
    """ Returns the imput of user (a new transaction amount) as a float"""
    # Get the user input, transform it from a string to a float and store it
    user_input = float(input('Your Transaction amount: '))
    return user_input

# Get the first transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

# Get the third transaction input and add the value to the blockchain
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

# Output the blockchain list to the console
for block in blockchain:
    print('Outputting Block')
    print(block)

print('Done')