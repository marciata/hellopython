# Strings e tuplas são sequencias imutaveis

#String
nome = "Marcia"
# imprime r
print(nome[2])
# da um erro pois nao é possivel mudar a string
#nome[2] = "b" # TypeError: 'str' object does not support item assignment

#Tuplas
# é igual lista, mas fica entre parenteses e nao pode ser alterado, ou seja, imutavel
tupla = ("elem1", "elem2", "elem3")
print(tupla[1]) # imprime elem2

# para criar uma tupla de um elemento so, é preciso colocar uma virgula no final para nao ser
# confundido com um elemento entre parenteses
tuplaUmElemento = ("alone", )
print(tuplaUmElemento)

# da erro pois tupla é imutavel
#tupla[1] = "elem5" # TypeError: 'tuple' object does not support item assignment

# é possivel transformar tupla em lista
lista = list(tupla)
print(lista[1])
print(type(lista))
lista[1] = "2" # não da erro pois agora é uma lista e listas sao mutaveis

tupla2 = tuple(lista) # transformando lista em tupla
print(type(tupla2))

listStr = list("Hello world") # transformando string em lista
print(listStr)

tupleStr = tuple("Hello world") # transformando string em tupla
print(tupleStr)

# listas sao passadas por referencia, tuplas e string sao passadas por valor