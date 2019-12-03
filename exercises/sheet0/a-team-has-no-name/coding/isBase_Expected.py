#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:33:12 2019

@author: daniel
"""

import os
from time import time
#from operator import itemgetter

def valueOf(B1):
    s = 0
    for j in B1:
        s += 2**j
    return s

def setOfValues(B):
    l = []
    for i in range(len(B)):
        l.append(valueOf(B[i]))
    return set(l)

def isBase(B, Set): #Function that checks if B is a base
    big = len(B)>100
    
    tenth = len(B)//10
    verifies = True
    for i in range(len(B)):#Loop that goes through all the sets in B
        if not verifies:
            continue
        if big:#This will print the the state of the process if the argument to be processed is really big
            if i%tenth == 0:
                print("estado: {}0%".format(i//tenth))
                
                
        for j in range(len(B)):#Loop that check all the other sets in B
            if j == i:
                continue
            if not verifies:
                break
            
            for k in range(len(B[i])): #And check if for one element in the first one the condition holds
                if not verifies:
                    break
                
                found = False
                e = B[i][k]
                if e in B[j]:
                    continue
                Bi = B[i][:k]+B[i][k+1:]
                for l in B[j]:
                    if found:
                        break
                    if l in Bi:
                        continue
                    
                    value = valueOf(Bi+[l])
                    found = value in Set
                    
                verifies = found#that base is ok if we find an element that verifies the condition
                if not verifies:
                    print("Elements {} and {} do not verify the condition".format(B[i],B[j]))
    return verifies


#charge the basis from their files
path = "/home/daniel/Documentos/CompGeometryJulian/2019-dag-upc/exercises/sheet0/matroid-or-not" 
fileList = []
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        fileList.append(entry)
        
listOfBases = []

for i in fileList:
    filename = path + "/" + i
    file = open(filename, 'r')
    base_i = []
    for line in file:
        columns = line.split()
        if columns[0] == "#":
            continue
        columnsInts = []
        for i in columns:
            columnsInts.append(int(i))
        base_i.append(columnsInts)
    listOfBases.append(base_i)
order = [2,9,6,10,7,11,0,4,1,8,5,3]

#loop trhough the set of potential basis that runs the program over them
#BEWARE: it will take A LOT of time, do not run if you cannot stop it before it ends.
#I had to wait more than five hours to run the better half of them
for i in order:
    print("fichero {}: {}".format(i,fileList[i]))
    B = listOfBases[i]
    t = time()
    l = setOfValues(B)
    print(isBase(B,l))
    print("{} seconds".format(time()-t))
        