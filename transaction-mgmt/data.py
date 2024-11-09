import random
import numpy as np
import pandas as pd
import resource

# TODO: create a DBMS design - how will we represent accounts and access our data efficently?
class HDD:
    def __init__(self):
        pages = 0
        page_size=resource.getpagesize() # number of bytes in a page
        record_size=None # number of bytes in a record


class Bank: 
    def __init__(self):
        client_count= 0



class Account: # Xact = a transaction
    ["name","usr-id","account_num","balance","transaction","transaction_date"])
    def __init__(self):
        name=None
        usr_id = random.randint()
        pass    
