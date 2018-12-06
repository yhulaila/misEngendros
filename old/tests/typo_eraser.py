# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:13:02 2017

Place the typo_eraser file into the directory
you need to clean the PDS3 data

@author: Julia Marín-Yaseli de la Parra (JUMP)
julia.marin@esa.int
"""
import glob
import fileinput
import sys
import re
from planetaryimage import PDS3Image

try:
    route = re.findall('.*/.*?', sys.argv[0] )
    route = (str(route[0]) + "*.IMG")
    archivos = glob.glob(route)
    archivos.sort()


    for linea in range(0,len(archivos)):

        print (archivos[linea])

    #if not fileinput.isfirstline():
     #   sys.stdout.write(linea)
     #   typo = re.findall('.*SPICE_FILE_NAME.*?/* GEOREFERENCING */?', archivos[linea])
     #   print (typo)


    archivo = open(archivos[linea], 'rb')
    linea = archivo.readline()
    while linea:
        print (linea[:len(linea) - 1])
        linea = archivo.readline()
        archivo.close()

except IOError:
    print('IOError')

