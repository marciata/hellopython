# o certo é criar com a extensao pyw para nao abrir um console qdo executar
# para criar um atalho, criar um arquivo .bat com o conteudo @pyw.exe multiclipboard.pyw %*

# essse programinha grava valores do clipboard num shelve e associa com uma chave e recupera
# o conteudo copiado, e joga no clipboard, de acordo com a chave informada
# usage: py.exe multiclipboard.pyw save <palavra-chave> - Salva clipboard na palavra-chave
#        py.exe multiclipboard.pyw <palavra-chave> - Carrega palavra-chave no clipboard
#        py.exe multiclipboard.pyw list - Carrega todas as palavras-chave no clipboard

import shelve, pyperclip, sys

# Cria um novo arquivo shelve chamado mcb
mcbShelf = shelve.open('mcb')

# Salva conteudo do clipboard
# pega o primeiro argumento (o arqumento 0 é o nome do programa)
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # copia o conteudo do clipboard e joga na chave informada no 3 parametro
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # Se foi passado so um parametro, entao é list ou a chave para buscar
    if (sys.argv[1].lower() == 'list'):
        # copia todo o conteudo gravado no shelve para o clipboard
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        # copia o conteudo da chave informada no argumento para o clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()