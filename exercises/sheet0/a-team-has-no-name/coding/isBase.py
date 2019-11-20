#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:33:12 2019

@author: daniel
"""

import os
from time import time
from operator import itemgetter

def setsToMasks(B):
    l = []
    for i in range(len(B)):
        s = 0
        for j in B[i]:
            s += 2**j
        l.append([i,s])
    return l

def compare_by(A,B,index):
    if A[index]<B[index]:
        return int(-1)
    elif A[index]==B[index]:
        return int(0)
    else:
        return int(1)

def sort_by(list, index):
    return sorted(list, key = itemgetter(index))

def orderBase(l,B):
    l_sets = []
    l_mask = []
    l1 = sort_by(l,1)
    for i in l1:
        l_mask.append(i[1])
        l_sets.append(B[i[0]])
    return l_mask, l_sets

def binarySearch(e,L,pos0,posF):
    half = (pos0+posF)//2
    if e < L[pos0] or e > L[posF-1]:
        return -1
    if e < L[half]:
        return binarySearch(e,L,pos0,half)
    elif e > L[half]:
        return binarySearch(e,L,half,posF)
    return half

def isBase(B, masks): #Function that checks if B is a base
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
                    
                    value = masks[i]-(2**e)+(2**l)
                    
                    bill_checked = binarySearch(value,masks,0,len(masks))#Check if B3 is in B with a Binary search
                    found = bill_checked >= 0
                    
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
    l = setsToMasks(B)
    l_ordered, B_ordered = orderBase(l,B)
    #print(l_ordered, B_ordered)
    print(isBase(B_ordered,l_ordered))
    print("{} seconds".format(time()-t))
        