import copy

def recebLista(arg):
    # aqui foi recebido a referencia da lista
    arg[0] = "novo"

lista = [1,2,3]
recebLista(lista)
# a lista original foi alterada
print(lista)

# para copiar a lista ao inves de passar referencia, usar a funcao copy.copy
# se a lista tiver lista, sera preciso usar a funcao copy.deepcopy
recebLista(copy.copy(lista))



def recebTupla(arg):
    arg[0] = "novo" # nao pode alterar tupla

tupla = ("a","b","c")
#recebTupla(tupla)
print(tupla)

