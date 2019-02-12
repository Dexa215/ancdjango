### LISTA
listaprova = ["Mauro","De Salvatore",26,1,1978]
print (listaprova)
print()

### accesso ad elemento > conteggio POSITIVO
### primo elemento          0
print("listaprova > elemento  0 :" + listaprova[0])
print("listaprova > elemento  1 :" + listaprova[1])
print("listaprova > elemento  2 :" + str(listaprova[2]))
print("listaprova > elemento  3 :" + str(listaprova[3]))
print("listaprova > elemento  4 :" + str(listaprova[4]))
print()

### acc ad elemento > conteggio NEGATIVO
### ultimo elemento         -1
print("listaprova < elemento -1 :" + str(listaprova[-1]))
print("listaprova < elemento -2 :" + str(listaprova[-2]))
print("listaprova < elemento -3 :" + str(listaprova[-3]))
print("listaprova < elemento -4 :" + listaprova[-4])
print("listaprova < elemento -4 :" + listaprova[-5])
print()

### parte di una lista
print (listaprova[0:3])
print (listaprova[1:4])
print (listaprova[2:5])

### parte di una lista
print (listaprova[0:3])
print (listaprova[1:4])
print (listaprova[2:5])

### FINO ad     elemento 3
print ("FINO AL 3 ELEMENTO :" + str(listaprova[:3]))

### DA          elemento 2
print ("DA ELEMENTO 2 :" + str(listaprova[2:]))

print("ïnizio ciclo for ...")
for el in listaprova:
    print (el)

mialista = list(range(0,10))
for el in mialista:
    print ("elemento "+ str(el))
    print (mialista.index(el))
    print (mialista)
print()

print("list: > " + str(list(range(10,21))))
print("tuple:> " + str(tuple(range(10,21))))
print("set:  > " + str(set(range(10,21))))
print()

### TUPLE
listaprova2 = 1,4,4,5,6,6
setprova=set(listaprova2)
print('listaprova: ')
print(listaprova2)
print(type(listaprova2))

### SET
print('setprova: ')
print(setprova)
print(type(setprova))
print()

### DICTIONARY
dict={'name':'mauro','surname':'de salvatore'}
print('dictionary : ')
print(dict)
print("dict name    : > " + str(dict.get('name')))
print("dict surname : > " + str(dict.get('surname')))