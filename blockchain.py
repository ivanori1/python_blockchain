# Initializing our (empty) blockchain list
MINING_REWARD = 10
genesis_block = {
                 
        'previous_hash': '',
        'index': 0,
        'transaction': [],
        
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Bozo'
participants = {'Bozo'}

def hash_block(block):
    return '-'.join([str(block[key] for key in block)])
    
def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transaction'] if tx['sender']== participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transaction'] if tx['recipient']== participant] for block in blockchain]
    tx_sender.append(open_tx_sender)
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent
def get_last_blockchain_value():
    """ Return the last value of the current bolckchain"""
    if len(blockchain) <1:
        return None
    return blockchain[-1]

# This function accepts two arguments,
# One requred one(transaction_amount) and the optional (last_transaction)
# Last ransaction is optional because it have default [1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']
        


def add_transaction(recipient, sender = owner, amount= 1.0):
    """ Append a new value as also the last transaction to blockchain
    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins
        :amount: The amount of coints send with transaction (default is 1 coin)
    """

    transaction = {
                   'sender': sender,
                   'recipient': recipient,
                   'amount': amount,
                   }
    if not verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD,
    }
    copied_transactions = open_transactions[:]
    open_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transaction': open_transactions,
        }
    blockchain.append(block)
    return True

def get_transaction_value():
    """ Returns the imput of user (a new transaction amount) as a float"""
    # Get the user input, transform it from a string to a float and store it
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your Transaction amount: '))
    return tx_recipient, tx_amount

def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('_'*20)


def verify_chain():
    """ Verify the current blockchain and return True if's valid, False if not"""    
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
    return True

def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])

waiting_for_input = True

# A while loop for the user input interface
# It's a loop that exist once waiting_for_input becomes False or when break appears
while waiting_for_input:
    print('Please choose: ')
    print('1) Add new transaction value')
    print('2) Mine new block')
    print('3) Output the blockchain blocks')
    print('4) Output the participants')
    print('5) Check Transaction validity')
    print('h) Manipulate the chain')
    print('q) Quit')

    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add Transaction amount to the blockchain
        if add_transaction(recipient, amount= amount):
            print('Added Transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid!')
        else:
            print('There are invalid transactions!')
    elif user_choice == 'h':
        # Make sure that you don't try to 'hack' the blockchain
        if len(blockchain) >= 1:
            blockchain[0] = {
                 
        'previous_hash': '',
        'index': 0,
        'transaction': [{'sender': 'DK', 'recipient': 'Migo', 'amount': 97000.0}],
        }
    elif user_choice == 'q':
        # This will lead to the loop to exit because runing condition become False
        waiting_for_input = False

    else:
        print('Input was invalid please put a value from the list!') 
    print('Choice Registered!')
    if  verify_chain():
        print(print_blockchain_elements)
        print('Invalid Blockchain')
        break
    print(get_balance(owner))
else:
    print('User left')
print('Done!')

