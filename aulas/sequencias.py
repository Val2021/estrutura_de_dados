# listas são mutaveis

lista = [1,3,5]
print(id(lista))
lista.append(6)
print(id(lista))
print(lista)

#Sequencias imutáveis

tupla = (1,2)

print(type(tupla))
print(id(tupla))
tupla +=(2,4)
print(id(tupla))

print("#Mutando imutavel com elementos mutaveis")

tupla = (lista,)
print(tupla)
print(id(tupla[0]))
lista.append(6)
print(tupla)
print(id(tupla[0]))