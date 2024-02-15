import threading
from irpytest1pypy import system
import uitest
import faultysearch
import pickle

import data
#import timesetting
from timesetting import timeset
import time
import login

filename='espip.pkl'
tfile="datetime.txt"
def loadfrom_file(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return None
if login.check()==1:
    
    espip=loadfrom_file(filename)
    flag = threading.Event()
    st=threading.Thread(target=system, args=(espip,flag,))
    st.start()
    uitest.gui(espip)
    flag.set()
    st.join()
    print("Server Clossed")
    