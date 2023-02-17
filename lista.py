# Sintaksa e listave:
lista = []
print(type(lista))

lista = [1, 1.1, 'string', True,['lista2',1],(),{}]
print(lista)
lista[1] = 2.2
print(lista)

# Printimi i elementeve te listes
for i in lista:
    print(i)

for i in [1,2,3,45]:
    print(i)

n = 0
while n < len(lista):
    print(lista[n])
    n +=1 # inkremento me 1

# Operimi +

lista_1 = [1,2,3]
lista_2 = [3,4,5]
lista_3 = lista_1+lista_2
print(lista_3)

# Prerja e listes
lista_4 = lista[0:3]
print(lista_4)

#Funksionet
## Shtimi i nje elementi

lista_5 = [1,2,3,"string", True]
lista_5.append([1,2])
print('Append:', lista_5)
## Fshirja e nje elementi
lista_5.pop(2) # largon elementin me indexin brenda kllapave
print("Pop: ",lista_5)
## Fshirja e nje elementi
lista_5.remove(1) # largon elementin me vleren brenda kllapave
print("Remove: ",lista_5)
## sort
lista_e_parenditur = [3,2,5,6,7,9,10,22,440,220]
print('Unsorted: ',lista_e_parenditur)
lista_e_parenditur.sort()
print("Sort: ",lista_e_parenditur)

lista_2D = [[1,2,3],
            [4,5,6],
            [7,8,9]]


for i in lista_2D:
    print(i)
    # for j in i:
    #     print(j)



