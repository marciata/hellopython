def monta_lista(totalElementos):
    lista = []
    for i in range(totalElementos):
        # inclusao pode ser via metodo insert = para quando inserir em posicao especifica
        #lista.insert(i, 'elem' + str(i))
        elem = 'elem' + str(i)
        # ou concatenacao de listas
#        lista = lista + [elem]
        # ou via metodo append (elemento é adicionado por ultimo na lista
        lista.append(elem)
    return lista

def print_lista(lista):
    # for percorrendo cada elemento da lista e imprimindo
#    for i in lista:
#        print(i)
    # for pegando o indice de cada elemento da lista e imprimindo
    for i in range(len(lista)):
        print('Indice ' + str(i) + "=" + str(lista[i]))

def print_primeiro_elemento(lista):
    print('Primeiro elemento: ' + str(lista[0]))

def print_ultimo_elemento(lista):
    print('Ultimo elemento: ' + str(lista[-1]))

def monta_lista_de_lista():
    lista = [[1,2], [3,4],[5,6]]
    return lista

def imprime_parte_lista(lista):
    print("imprime elementos 2 a 4 excluindo 4 (slice = parte de uma lista. É retornada como uma nova lista)")
    print(lista[2:4])
    print("imprime elementos 0 até -1 excluindo -1 que no caso é o ultimo elemento")
    print(lista[0:-1])
    print("imprime elementos 5 até ultimo elemento")
    print(lista[5:])
    print("imprime inicio da lista até 4 exclusive")
    print(lista[:4])

def altera_valor_lista(lista, posicao):
    lista[posicao] = "novo elemento"
    print(lista[posicao])

def concatena_listas():
    lista1 = [1,2,3]
    lista2 = [4,5,6]
    lista_total = lista1 + lista2
    print(lista_total)

def multiplica_listas():
    lista1 = [1,2,3]
    print(lista1 * 3)

def deletando_elem():
    lista1 = [1,2,3,4]
    # remocao pode ser via del
    del lista1[2]
    # ou via remove = nesse caso remove por valor
    lista1.remove(4)
    print(lista1)

def atribuicao_multipla():
    lista1 = [1,2,3]
    # os elementos da lista sao atribuidos as variaveis na ordem. Se tiver menos elementos que atributos, erro
    a, b, c = lista1
    print('a=' + str(a), 'b=' + str(b), 'c=' + str(c))

def ordenacao_lista():
    lista1 = [2,6,4,3,9,1,8]
    # metodo sort pode ser em int ou strings. nao pode ser em lista com int E string
    # ordenacao é in place, ou seja, na propria lista
    # ordenacao baseada na tabela asc, maiusculo > minusculo
    # ordem crescente
    lista1.sort()
    print(lista1)
    #ordem decrescente
    lista1 = ['a', 'f', 'e', 'r', 't']
    lista1.sort(reverse=True)
    # ordenar sem considerar tabela asc
    lista1.sort(key=str.lower)

lista_montada = monta_lista(10)
print_lista(lista_montada)
print_primeiro_elemento(lista_montada)
print_ultimo_elemento(lista_montada)
print_lista(monta_lista_de_lista())
imprime_parte_lista(lista_montada)
print("Tamanho da lista: " + str(len(lista_montada)))
print('Alteracao')
altera_valor_lista(lista_montada, 5)
print('novo elemento' in lista_montada)
print('novo elemento' not in lista_montada)
concatena_listas()
multiplica_listas()
print('Deletando: ')
deletando_elem()
print('Atribuicao múltipla')
atribuicao_multipla()
ordenacao_lista()
