import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    # inclui a chave no dicionario inicializando com zero
    count.setdefault(character, 0)
    # soma a quantidade de caracteres do texto
    count[character] = count[character] + 1

# para imprimir de forma mais elegante o conteudo do dicionario
pprint.pprint(count)