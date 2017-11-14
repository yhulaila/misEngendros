import re

archivo = open('test.txt', 'r')
linea = archivo.readline()
output = re.sub(r'\(?=\d)', r'/', linea)

print (output)