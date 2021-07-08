

"""
Torre de hanoi
*Algoritmos recursivos possuem condição óbvia de parada


"""

contage_de_chamadas_recursivas = 0

def torre_de_hanoi(numero_de_discos: int):
    _torre_de_hanoi_recursivo(numero_de_discos,origem='A',destino = 'B',auxiliar = 'C')
  

def _torre_de_hanoi_recursivo(numero_de_discos,origem,destino ,auxiliar):
    global contage_de_chamadas_recursivas
    contage_de_chamadas_recursivas +=1
    if numero_de_discos == 1:
        print(f'{origem} => {destino} : {numero_de_discos}')
        return
    _torre_de_hanoi_recursivo(numero_de_discos -1,origem,auxiliar,destino)
    print(f'{origem} => {destino} : {numero_de_discos}')
    _torre_de_hanoi_recursivo(numero_de_discos -1,auxiliar,destino,origem)



if __name__ == '__main__':
    for i in range(1,5):
        print(f'#### hanoi para {i} discos')
        torre_de_hanoi(i)

        print(f'****{contage_de_chamadas_recursivas} chamadas')
       