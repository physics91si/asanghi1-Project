#!/anaconda/bin/python
import numpy as np
import random as random 
#generate strings that only use chars "a", "g", "t", or "c" and are 70 chars long. Generate between 50 and 500 strings 
def generateReads():
    numberReads=np.rint((np.random()*500),0)
    if numberReads <= 50:
        numberReads=50
    i=0
    read=None
    listReads=[]
    lengthOverlap=0
    while i <= numberReads:
        for x in range(0,(70-lengthOverlap)):
           letterGenerator= np.random()
           if letterGenerator < 0.25:
               letter="a"
           elif letterGenerator < 0.5:
               letter="g"
           elif letterGenerator < 0.75:
               letter="t"
           else:
               letter="c"
           read= read + letter
        listReads[i]=read
        randoIndex=np.rint((np.random()*70))
        stringHolder=listReads[i]
        listReads[i+1]=stringHolder[randoIndex:70]
        read=listReads[i+1]
        lengthOverlap=len(read)
        i += 1
    return random.shuffle(listReads)

#introduce random errors in reads
def error():
    
#order the reads by finding the overlapping regions. create a matrix that compares every character in read to matching position in the other reads. The highest matching string is the next read. 
def alignReads():
    listReads=generateReads()
    
        

    
    
