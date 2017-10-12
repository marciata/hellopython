# dicionario é como se fosse uma lista, mas cujas chaves podem ser definidas. Semelhante a Map do java ou
# objeto do javascript
dicionario = {"color": "Azul", "tamanho": "medio", "peso": 10, "idade": 12}
print(dicionario)

# para iterar entre as chaves do dicionario
for d in dicionario:
    print(d)
    print(dicionario[d]) # imprimir o valor

# se tentar acessar uma chave q nao existe, um erro sera lancado
# print(dicionario["chave"]) # KeyError: 'chave'

# para iterar sobre as chaves de um dicionario
for c in dicionario.keys():
    print(c)

# para iterar sobre os valores de um dicionario
for v in dicionario.values():
    print(v)

# para iterar sobre os items (chave: valor)
for i in dicionario.items():
    print(i)

# para pegar um valor default, caso nao exista nenhum, sem alterar o dicionario original
print(dicionario.get("chave", 1)) # a chave key nao existe, entao retornara 1 ao inves de dar um erro.
# O dicionario original nao é alterado
print(dicionario)

# para setar um valor default caso nao exista a chave informada
dicionario.setdefault("chave", 2)
# o dicionario original agora tem uma chave com valor 2
print(dicionario)
# agora o valor nao sera alterado pois a chave ja existe
dicionario.setdefault("chave", 3)
print(dicionario)

# a ordem dos itens no dicionario nao fazem diferenca
print({"a": 1, "b": 2, "c": 3} == {"b": 2, "a": 1, "c": 3}) # True

# a ordem dos itens na lista fazem diferenca
print([1, 2, 3] == [3,2,1]) # False