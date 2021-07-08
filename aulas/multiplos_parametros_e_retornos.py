def ponto():
    return 1,2

primeiro,segundo = ponto()
print(primeiro,segundo)

print("-----------------------")

def gerar_ponto():
    return (1,2)

ponto=gerar_ponto()
primeiro,segundo = ponto #desempacotamento
print(primeiro,segundo)

print("-----------------------")



def gerar_ponto():
    return (1,2)

ponto=gerar_ponto()
primeiro, *_ = ponto #desempacotamento
print(primeiro,_) #retorna uma lista

print("-----------------------")

def argumentos_variaveis(*args):#empacotando argumentos posicionais
    print(args)
    print(type(args))

argumentos_variaveis(1)
argumentos_variaveis((1,2))#empacotamento
argumentos_variaveis(*(1,2))#desempacotamento
argumentos_variaveis(*[1,2])#desempacotamento serve para lista tb
argumentos_variaveis(*'valzinha')#desempacotamento serve para lista tb

for chave,valor in {'pt':'Portugues','en':'Ingles'}.items():
    print(chave)
    print(valor)