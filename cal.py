from curses.ascii import isdigit
delimit=','
import re

def Add(numbers):
    count=0
    neg=[]
    a=re.findall(r"-?\d+", numbers)
    numbers = list(map(int, a))
    if len(numbers) == 0:
        return 0
    
    print(numbers)
    for i in numbers:
        if(i<0):
            count=1
            neg.append(i)
    
    if count==0:
        return sum(numbers)
    else:
        raise Exception("negatives not allowed "+' '.join(map(str, neg)))



