# String podem ser escritas entre aspas simples e aspas duplas
print('String em aspas simples')

# Para incluir um texto com aspas simples, utilize aspas duplas para delimitar
print("That's a good example")

# É possível utilizar o caracter de escape \
print('That\'s a good example')

# É possivel utilizar o caracter r para indicar strings puras, ou seja, sem considerar caracteres de escape (raw strings)
print(r'That\s a good example\n') # imprime That\s a good example\n

# Para imprimir texto com espacos e tabulacoes, podem ser usados 3 aspas simples ou 3 aspas duplas como delimitador
print('''Isso vai imprimir
            com todos esses espacos
                e com caracter \ \\n nao é escapado ''')

"""Para incluir comentarios de varias linhas, pode ser usado 3 aspas tambem"""

#String slicing
spam = "Hello world!"
print(spam[2]) # imprime l
print(spam[2:5]) # imprime llo
print(spam[:5]) # imprime Hello
print(spam[2:]) # imprime llo world!

# in e not in
print('H' in 'Hello') # True
print('H' not in 'Hello') # False

# Métodos de String
# upper()
print('hello'.upper()) # imprime HELLO
# lower()
print('HEllo'.lower()) # imprime hello
# isupper() => imprime true se todos os caracteres forem maiusculos
print('HELLO'.isupper()) # imprime True
# islower() => imprime true se todos os caracteres forem minusculos
print('hello'.islower()) # imprime True

# isX String possui vários outros metodos no estilo is..
# isalpha = verifica se a string possui somente letras
print('hello'.isalpha()) # True
# isalphanum = verifica se a string possui somente letras e numeros
print('hello!'.isalnum()) # False
# isdecimal = verifica se a string possui somente numeros
print('123'.isdecimal()) # True
# isspace = verifica se a string possui apenas espacos
print(' '.isspace()) # True
# istitle = verifica se as palavras da string comecam com maiusculo seguido de minusculos
print('Isso É Um Titulo'.istitle()) # True

# startswith() = verifica se a string comeca com o valor passado
print('Hello world'.startswith('Hello')) # true
# endswith() = verifica se a string termina com o valor passado
print('Hello world'.endswith('world')) # True

# join = para unir uma lista de strings em uma unica string com um separador especifico
print(','.join(['cats', 'rats', 'bats'])) # imprime a string 'cats, rats, bats'

# split = para separar uma string em uma lista de strings
print("cats, bats, rats".split(', ')) # retorna a lista ['cats', 'bats', 'rats']
# imprime ['Para separar ', '        um texto identado e cheio', '        de quebras de linhas em', '        uma lista']
print('''Para separar 
        um texto identado e cheio
        de quebras de linhas em
        uma lista'''.split('\n'))

# rjust() justifica o texto a direita
print('Hello'.rjust(10)) # vai imprimir 5 espacos em branco e a palvra Hello (totalizando 10 caracteres)
print('Hello'.rjust(10, '*')) # vai imprimir 5 * e a palvra Hello (totalizando 10 caracteres)

# ljust() justifica o texto a esquerda
print('Hello'.ljust(10)) # vai imprimir a palavra Hello e 5 espacos (totalizando 10 caracteres)
print('Hello'.ljust(10, '*')) # vai palavra Hello e 5 * (totalizando 10 caracteres)

# center = imprime o texto no centro
print('Hello'.center(11)) # vai imprimir 3 espacos, a palavra Hello e 3 espacos (totalizando 11 caracteres)
print('Hello'.center(11, '*')) # vai imprimir 3 *, a palavra Hello e 3 * (totalizando 11 caracteres)

# strip() = remover caracteres vazios, quebra de linha ou tabulacao
print('   Hello   '.strip()) # imprime Hello sem espacos

# lstrip()= remover caracteres vazios a esquerda
print('   Hello   '.lstrip()) # imprime Hello     somente com espacos a direita

# rstrip()= remover caracteres vazios a direita
print('   Hello   '.rstrip()) # imprime     Hello somente com espacos a esquerda

# para especificar os caracteres q devem ser removidos
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS')) # imprime BaconSpamEggs a ordem dos caracteres a ser removidos nao importa
print('SpamSpamBaconSpamEggsSpamSpam'.strip('mapS')) # imprime BaconSpamEggs a ordem dos caracteres a ser removidos nao importa
print('SpamSpamBaconSpamEggsSpamSpam'.strip('Spam')) # imprime BaconSpamEggs a ordem dos caracteres a ser removidos nao importa
