#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:43:47 2019

@author: daniel
"""
import os
from time import time

def contained(L1,L2):#Function that checks if L1 is contained in L2
    boolean = True
    for e in L1:
        if not boolean:
            continue
        boolean = e in L2
    return boolean

def belongs(L,LL):#Function that checks if L1 is contained in one of the sets in LL
    found = False
    for i in LL:
        if found:
            continue
        found = contained(L,i)
    return found

def isBase(B): #Function that checks if B is a base
    big = len(B)>100
    
    validPairs = [[] for i in range(len(B))]#list of the pairs that do not need to be checked
    tenth = len(B)//10
    cumple = True
    for i in range(len(B)):#for all the sets in B
        if not cumple:
            continue
        if big:
            if i%tenth == 0:
                print("estado: {}0%".format(i//tenth))
                #print(len(validPairs))
                
        for j in range(len(B)):#check all the other lists
            if j == i:
                continue
            if not cumple:
                continue
            already_checked = False
            for pair in validPairs[i]:#we check if we do not need to check this pair
                if already_checked:
                    continue
                already_checked = j == pair
            
            if already_checked:
                continue
            
            for k in range(len(B[i])): #and check if for one element in the first one the condition holds
                if not cumple:
                    continue
                
                found = False
                e = B[i][k]
                if e in B[j]:
                    continue
                Bi = B[i][:k]+B[i][k+1:]
                for l in B[j]:
                    if found:
                        continue
                    if l in B[i]:
                        continue
                    Bil = Bi+[l]
                    bill_checked = False
                    for b in range(len(B)):
                        if bill_checked:
                            continue
                        if contained(Bil,B[b]):
                            already_added = False
                            for pair in validPairs[i]:
                                if already_added:
                                    continue
                                already_added = j == pair
                                
                            
                            if not already_added:
                                validPairs[i].append(j)
                                validPairs[j].append(i)
                            bill_checked = True
                            #print("{} obtained from {} and {} is in {}".format(Bil,B[i],B[j],b))
     
                    found = bill_checked
                    #print("{} obtained from {} and {} is in {}".format(Bil,B[i],B[j],b))
                cumple = found#that base is ok if we find an element that verifies the condition
                if not cumple:
                    print("Elements {} and {} do not verify the condition".format(B[i],B[j]))
    return cumple

#simple base to check
B1 = [[1,2,3],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5]]



isBase(B1)


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
#BEWARE: it will take TONS of time, do not run if you cannot stop it before it ends.
#I had to wait more than five hours to run the better half of them
for i in order:
    print("fichero {}: {}".format(i,fileList[i]))
    t = time()
    print(isBase(listOfBases[i]))
    print("{} seconds".format(time()-t))
        
