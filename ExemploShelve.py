# shelve cria um arquivo binario que pode ser utilizado para gravar dados de configuracao de um programa
import shelve as s
# vai abrir ou criar um arquivo. Abrira em mode de leitura e escrita
shelfFile = s.open('myconfig')
# apenas uma lista comum
cats = ['Zophie', 'Pooka', 'Simon']
# gravando uma chave cats com a lista de gatos
shelfFile['cats'] = cats
# grava o arquivo e fecha
# isso irá criar 3 arquivos. myconfig.bak, myconfig.dat e myconfig.dir
shelfFile.close()

# se rodar s.open de novo, o arquivo sera aberto
myconfig = s.open('myconfig')
# imprime <class 'shelve.DbfilenameShelf'>
print(type(myconfig))
# imprime ['Zophie', 'Pooka', 'Simon']
print(myconfig['cats'])

# para mudar os valores gravados no shelve
myconfig['cats'] = ['Garfield', 'Felix', 'Snowball']

print(myconfig['cats'])

myconfig.close()