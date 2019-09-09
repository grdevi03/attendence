import time
import numpy as np
import pandas as pd
import datetime
import logging

while True:
    sec = np.random.randint(1,5)
    time.sleep(sec)
    print("Slept for {} seconds".format(sec))
    #data_dt = time.strftime("%Y-%m-%d-%H.%M.%S",time.localtime())
    data_id = np.random.randint(low=1001,high=1026,size=1)[0]
    logging.basicConfig(filename='./devi.log',format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('INFO: Person Id={}'.format(data_id))
    #print('date :',data_dt)
