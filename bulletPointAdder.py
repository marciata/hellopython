# programa para adicionar os marcadores de lista da wiki ( * para cada item da lista) tendo como entrada
# um texto do clipboard com quebras de linha sendo que cada quebra sera um item da lista
import pyperclip

text = pyperclip.paste()

# Separa as linhas e acrescenta *
lines = text.split('\n')
for i in range(len(lines)): # percorre todos os indices da lista "lines" em um loop
    lines[i] = '* ' + lines[i] # acrescenta um * em cada string da lista "lines"
text = '\n'.join(lines)
pyperclip.copy(text)

