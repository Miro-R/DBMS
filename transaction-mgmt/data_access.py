class Xact: # Xact = a transaction
    def __init__(self):

        pass    

def access_request(account): # UPDATE account, SET balance, WHERE account_num=



def read_page():
    pass

def write_page():
    
    pass


def build_schedule():
    pass


def commit():

    pass

def abort():
    pass

# ACID testing

def consistency_check():
    pass

def isolation_check():
    pass

## Logging and Recovery
def durability_check():
    pass

def atomicity_check():
    # Idea: either all of the parts of a transaction is done OR NONE of them
    pass


def ACID_test():
    logging_and_recovery = (durability_check() and atomicity_check())
    concurrency_control = (consistency_check() and isolation_check())

    if (logging_and_recovery and concurrency_control):
        return True
    else:
        return False