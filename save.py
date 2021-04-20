#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. STRING_ARRAY labels
#  3. INTEGER dailyCount
#

def maxCost(cost, labels, dailyCount):
    d={}
    for i in range(len(cost)):
        d[cost[i]]=labels[i]
        
    
    i=0    
    
    
    legcount=0
    tc=0
    totalcount=0
    while i<len(cost):
        
            
        if d[cost[i]]=="legal":
                legcount+=1
        
        tc+=cost[i]
        
        if legcount>=dailyCount:
            if tc>totalcount:
                totalcount=tc
            legcount=0
            tc=0
        i+=1
    
    return totalcount
        
    # Write your code here

if __name__ == '__main__':
