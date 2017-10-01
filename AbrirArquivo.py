path = "palavras.txt"

# abrindo um arquivo em modo de escrita - parametro w
# se o arquivo ja existir, vai fazer append, caso contrario, vai criar
arquivo = open(path, "w")
# escrevendo no arquivo
arquivo.write("banana\n")
arquivo.write("abacaxi\n")
arquivo.write("laranja\n")
arquivo.write("melancia\n")
arquivo.write("uva\n")
# fechando o arquivo
arquivo.close()

# abrindo um arquivo - parametro r
arquivo = open(path, "r")
for palavra in arquivo :
    print(palavra.strip()) # strip vai tirar qq caracter especial, no caso o \n

arquivo.close()

