route1 = 'data/W20150511T083550851ID30F18.IMG'
print(route1)
route2 = 'cache' + str(route1[4:31]) + '.txt'


file =  open('data/list.txt')
print(file)
file = file.readlines()
route =[]
for line in file:
    print(line, type(line))
    route.append('data/'+line)

print (route)

for i in range(0,len(route)):
    print('fichero ejecutandose:   ', route[i])
    main(str(route[i]))
    print('fichero terminado:   ', route[i])