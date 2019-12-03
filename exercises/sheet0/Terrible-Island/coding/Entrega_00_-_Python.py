# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:23:25 2019

@author: Arnau
"""
import os

def procesar(linea):
    linea = linea.strip()
    return set(int(numero) for numero in linea.split(' '))
                    

            
def esmatroide(bases):
    for conjunto1 in bases:
        for conjunto2 in bases:
            if(conjunto1 == conjunto2):
                break
            c1 = conjunto1 - conjunto2
            c2 = conjunto2 - conjunto1
            for x in c1:
                exists = False
                semi_conjunto = conjunto1-{x}
                for y in c2:
                    if semi_conjunto|{y} in bases:
                        exists=True
                        break
                if exists == False:
                    return False
    return True

directorio = "C:\\Users\\Arnau\\Desktop\\matroid-or-not\\"
ficheros = [directorio + fichero for fichero in os.listdir(directorio)][2:3]
print(ficheros)
for ruta in ficheros:                        
    with open(ruta,"r") as fichero:
        bases = [procesar(linea)
                 for linea in fichero
                 if not linea.startswith("#")] 
        print('Fichero {}: Es matroide? {}'.format(ruta, esmatroide(bases)))
