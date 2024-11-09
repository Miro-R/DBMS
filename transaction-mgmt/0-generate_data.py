import numpy as np
import pandas as pd

CLIENT_COUNT = 100
NAM_MAX = 48804

def main():
    rng = np.random.default_rng()
    ints=rng.integers()
    bankData=pd.DataFrame(columns=["name","usr-id","account_num","balance","transaction","transaction_date"])
    


if __name__ == "__main__":
    main()


    # GOAL: implement this weeks transaction management 
    # TODO:
    # - [ ] Generate fake bank data
    # - [ ] Compare concurrent data access vs non-concurrent data access throughput
    # - [ ] create HDD folder
    # - [ ] write create page function 
    # - [ ] write a Read Page function
    # - [ ] write a Write page function