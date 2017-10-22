import os

# o método os.path.join monta o caminho do diretorio com \ ou /, dependendo do os
print(os.path.join('user', 'bin', 'spam')) # no caso do windows, imprime user\bin\spam no console imprime \\ p escapar a \

# imprime o diretorio atual
print(os.getcwd())

# muda o diretorio atual
#os.chdir('C:\\tools')
#print(os.getcwd())

# para criar um diretorio ou hierarquia de diretorios
#os.makedirs('C:\\tools\hellopython\exercicios') # se o diretorio ja existe, da um erro

# retorna o caminho absoluto de um caminho relativo
print(os.path.abspath('.'))

# retorna se o valor informado é um valor absoluto ou relativo
print(os.path.isabs('.'))

# retorna o caminho relativo de um diretorio, dado o caminho de referencia
print(os.path.relpath('C:\\tools', 'C:\\Users'))

# retorna o diretorio (tudo que estiver antes da ultima barra)
print(os.path.dirname(os.getcwd())) # C:\tools

# retorna tudo que estiver depois da ultima barra
print(os.path.basename(os.getcwd())) # hellopython

# retorna o conteudo antes da ultima barra e conteudo depois da ultima barra na forma de uma tupla
print(os.path.split(os.getcwd())) # 'C:\\tools', 'hellopython')

# para retornar cada diretorio separado, utilizar o split de string
# os.path.sep incluira os separadores de acordo com o so
print(os.getcwd().split(os.path.sep)) # ['C:', 'tools', 'hellopython']

# retorna o tamanho de um arquivo em bytes
esseArquivo = os.path.getsize(os.getcwd() + os.path.sep + 'ExemploFile.py')
print(esseArquivo)

# retorna a lista de arquivos do caminho informado
print(os.listdir(os.getcwd()))

# retorna se o caminho existe ou nao
print(os.path.exists(esseArquivo))

# verifica se é um arquivo
print(os.path.isfile(esseArquivo))

# verifica se é um diretorio
print(os.path.isdir(str(esseArquivo)))

def lerArquivo(filename):
    # para ler arquivo, passar o parametro r. O caminho pode ser absoluto ou relativo
    # o default é modo de leitura
    # o arquivo nao pode ser alterado em modo de leitura
    file = open(filename, 'r')
    # para ler o conteudo completo do arquivo em forma de uma string
    # print(file.read())
    # para obter o conteudo como uma lista de strings
    print(file.readlines())
    # o arquivo deve sempre ser fechado apos o uso
    file.close()

def criarArquivo(filename, conteudo):
    # para escrever em arquivo, chamar open com o parametro w. Se o arquivo nao existir, sera criado
    # passando w, o arquivo sera sobrescrito toda vez
    # file = open(filename, 'w')
    # passando a, o conteudo sera adicionado no arquivo. se o arquivo nao existir, sera criado
    file = open(filename, 'a')
    # para escrever no arquivo
    file.write(conteudo)
    file.close()


filename = os.getcwd() + os.path.sep + 'exercicios' + os.path.sep + 'hellofile.txt'
print(os.getcwd() + os.path.sep)
#criarArquivo(filename, 'Hello world\n')
lerArquivo(filename)