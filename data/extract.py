import json
import glob
import pandas as pd

from os import path
from os import listdir


my_path = path.abspath(path.dirname(__file__))

productPath = path.join(my_path,"./product/ProductReference.csv")
transactionPaths = [path.join(my_path+"/transactions/",x) for x in listdir(my_path+"/transactions/")]

def getProducts():
    frame = pd.read_csv(productPath)
    return frame

def getTransactions():
    frame = pd.concat((pd.read_csv(file) for file in transactionPaths),ignore_index=True)
    return frame

#print(getTransactions())
#print(getProducts())

