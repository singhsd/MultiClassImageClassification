# -*- coding: utf-8 -*-
try:
    file1=open("results\TrainingResults.txt","r")
    lines=file1.readlines()
    good=0
    total=len(lines)/2
    for i in range(0,len(lines),2):
        x=lines[i]
        y=lines[i+1]
        x=x[:-1]
        y=y[:-1]
        #print(x+"*")
        #print(y+"*")
        if y in x:
            good=good+1
        else:
            print(x,y)
        #input()
    print(good,total)
finally:
    file1.close()
