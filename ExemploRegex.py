import re
def testeRegex1():
    texto = "Texto que sera usado para procurar o padrao 44 99999-9999"
    padrao = r'\d\d 9\d\d\d\d-\d\d\d\d'
    # para informar padroes de expressoes regulares, use r para que seja considerado o literal, ou seja raw string
    # se nao for utilizar r, sera necessario digita \\d\\d.. para escapar a barra invertida da expressao
    regex = re.compile(padrao)
    rs = regex.search(texto)
    if (rs == None):
        print('Padrao {} nao encontrado no texto {}'.format(padrao, texto))
    else:
        print('Texto encontrado:', rs.group())

def textRegex2():
    texto = "Texto que sera usado para procurar o padrao 44 99999-9999"
    # para agrupar os padroes em grupos, pasta incluir parenteses
    # caso seja necessario incluir parenteses no padrao, deve ser escapado com \
    padrao = r'(\d\d) (9\d\d\d\d-\d\d\d\d)'
    # para informar padroes de expressoes regulares, use r para que seja considerado o literal, ou seja raw string
    # se nao for utilizar r, sera necessario digita \\d\\d.. para escapar a barra invertida da expressao
    regex = re.compile(padrao)
    # search ira pegar a primeira ocorrencia que bate com o padrao.
    rs = regex.search(texto)
    # se chamar rs.group(0) ou rs.group() será retornado tudo
    print('Texto encontrado:', rs.group())
    # se chamar rs.group(1) será retornado 44, q é o primeiro grupo
    print('Texto encontrado:', rs.group(1))
    # se chamar rs.group(2) sera retornado 99999-9999 q é o segundo grupo
    print('Texto encontrado:', rs.group(2))
    # se chamar rs.groups() será retornado uma tupla
    print(rs.groups())

def textRegexGenerico(padrao, texto):
    regex = re.compile(padrao)
    rs = regex.search(texto)
    if (rs == None):
        print('Padrao {} não encontrado no text {}'.format(padrao, texto))
    else:
        print('Encontrado = {} no padrao {} no texto {}'.format(rs.group(), padrao, texto))

# site para testar regex http://regexpal.com
# para especificar um conjunto de opcoes que podem ser consideradas, utilizar |
# esse trecho considerara valido Batman, Batmobile, Batcopter e Batbat
padrao = r'Bat(man|mobile|copter|bat)'
textRegexGenerico(padrao, 'Batbat, Batman')

# o ? indica texto opcional. Nesse caso imprime Batman ou Batwoman
# outro exemplo é (\d\d)? \d\d\d\d\d-\d\d\d\d para encontrar telefones com ou sem ddd
# caso precise incluir ? no padrao, escapar com \
padrao = r'Bat(wo)?man'
textRegexGenerico(padrao, 'Batbat, Batman')

# o * indica texto ocorrendo 0 ou mais vezes. Nesse caso imprime Batman ou Batwoman ou Batwowowowoman
# caso precise incluir * no padrao, escapar com \
padrao = r'Bat(wo)*man'
textRegexGenerico(padrao, 'Batbat, Batman')

# o + indica texto ocorrendo 1 ou mais vezes. Nesse caso imprime Batwoman ou Batwowowowoman mas nao Batman
# caso precise incluir * no padrao, escapar com \
padrao = r'Bat(wo)+man'
textRegexGenerico(padrao, 'Batbat, Batman, Batwoman')

# Para indicar um numero especifico de repeticoes, colocar entre chaves
# nesse caso aceita Batwowowoman, mas nao Batwoman
padrao = r'Bat(wo){3}man'
textRegexGenerico(padrao, 'Batman, Batwoman, Batwowowoman')

# É possivel tambem especificar um numero minimo e maximo de ocorrencias
# nesse caso aceita Batwowoman e Batwowowoman, mas nao Batwoman
# também pode ser informado {,3} para indicar de zero a 3 ocorrencias, ou {3,} para 3 ou mais ocorrencias
padrao = r'Bat(wo){2,3}man'
textRegexGenerico(padrao, 'Batman, Batwoman, Batwowoman, Batwowowoman')

# por padrao, o python é greedy (guloso) ou seja, vai sempre procurar a maior string possivel, portanto,
# no caso abaixo, apesar de 3 Ha ja atenderem ao padrao, sera considerado o Ha 5 vezes
# para forcar que seja considerado 3 vezes, é preciso incluir um ?. Ex (Ha){3,5}?
padrao = r'(Ha){3,5}'
textRegexGenerico(padrao, 'HaHaHaHaHaHaHa')

def comFindAll(padrao, texto):
    regex = re.compile(padrao)
    # findAll retorna todas as correspondencias em uma lista de strings, caso nao tenha grupos, ou
    # uma lista de tuplas, caso tenha grupos
    rs = regex.findall(texto)
    if (rs == None):
        print('Padrao {} nao encontrado no texto {}'.format(padrao, texto))
    else:
        for i in range(len(rs)):
            print(rs[i])

# quando o padrao nao tem grupos, o retorno do findAll sera uma lista de strings
padrao = r'\d\d\d-\d\d\d'
comFindAll(padrao, 'Bla bla bla 123-456 bla bla bla 567-345')

# quando o padrao tem grupos, o retorno do findAll sera uma lista de tuplas
padrao = r'(\d\d\d)-(\d\d\d)'
comFindAll(padrao, 'Bla bla bla 123-456 bla bla bla 567-345')

def caracteresEspeciais():
    print(r'\d', 'Qualquer digito de 0 a 9')
    print(r'\D', 'Qualquer caractere que não seja um digito de 0 a 9')
    print(r'\w', 'Qualquer letra, digito ou underscore ')
    print(r'\W', 'Qualquer caractere que não seja letra, numero ou underscore')
    print(r'\s', 'Qualquer espaço, tabulação ou caractere de quebra de linha')
    print(r'\S', 'Qualquer caractere que não seja um espaço, uma tabulação ou uma quebra de linha')

# para especificar um conjunto especifico de caracteres, digitar entre colchetes
padrao = r'[12agc0]'
# intervalos de valores tbm sao aceitos
padrao = r'[a-z0-9]'
# os caracteres especiais não precisam ser escapados dentro dos colchetes
# nesse caso procurara a ou b ou c ou . ou ?
padrao = r'[abc.?]'
# para criar uma lista de caracteres que não deve estar presente no texto, usar ^
padrao = r'[abc]^'

# o ^ também pode ser usado para indicar um padrao que deve ocorrer no inicio do texto
# nesse caso o padrao bate, pois o texto tem hello no comeco
padrao = r'^Hello'
textRegexGenerico(padrao, 'Hello world')
# nesse caso nao bate pq hello nao esta no comeco da frase
textRegexGenerico(padrao, 'Outro Hello world')

# o $ funciona de forma semelhante, mas para indicar um padrao que deve ocorrer no fim do texto
# nesse caso o padrao bate, pois o texto tem hello no fim
padrao = r'Hello$'
textRegexGenerico(padrao, 'world Hello')
# nesse caso nao bate pq hello nao esta no comeco da frase
textRegexGenerico(padrao, 'Hello world')

# padrao para encontrar strings que comecem e terminem por um digito
padrao = r'^\d+$'
textRegexGenerico(padrao, '413325')

# o caracter . é um caracter curinga pois corresponde a qualquer caractere, exceto quebra de linha
# para incluir ponto no padrao, escape com \
padrao = r'.at'
comFindAll(padrao, 'The cat in the hat sat on the flat mat')

# . corresponde um unico caracter
# .* indica qualquer conjunto de caracteres
padrao = r'Texto (.*)'
comFindAll(padrao, 'Texto qualquer')

# para indicar qualquer conjunto de caracteres considerando o modo não greedy (não guloso), incluir um ?
padrao = r'Texto (.*?)'

# o caracter . corresponde a qualquer caracter exceto quebra de linha. Para
# que o compilador considere tambem a quebra de linha, passar o parametro re.DOTALL para o compile
re.compile(padrao, re.DOTALL)

def resumo():
    print('? corresponde a zero ou uma ocorrencia do grupo anterior')
    print('* corresponde a zero ou mais ocorrencias do grupo anterior')
    print('+ corresponde a uma ou mais ocorrencias do grupo anterior')
    print('{n} corresponde a exatamente n ocorrencias do grupo anterior')
    print('{n,} corresponde a n ou mais ocorrencias do grupo anterior')
    print('{,m} corresponde a zero até m ocorrencias do grupo anterior')
    print('{n,m} corresponde a no minimo n e no maximo m ocorrencias do grupo anterior')
    print('{n, m}? ou *? ou +? faz uma correspondencia nongreedy do grupo anterior')
    print('^spam quer dizer que a string deve começar com spam')
    print('spam$ quer dizer que a string deve terminar com spam')
    print('. corresponde a qualquer caractere, exceto os caracteres de quebra de linha')
    print(r'\d, \w e \s correspondem a um dígito, um caractere de palavra ou um caractere de espaço, respectivamente')
    print(r'\D, \W, e \S correspondem a qualquer caractere, exceto digito, um caracter de palavra ou um caracter de espaço, respectivamente')
    print('[abc] corresponde a qualquer caracter que estiver entre os colchetes (por exemplo, a, b, c)')
    print('[^abc] corresponde a qualquer caractere que nao esteja entre os colchetes')
    print()
    print('Para o regex considerar o ponto como qualquer caracter, inclusive quebra de linha, passar o parametro re.DOTALL como segundo parametro de re.compile')
    print('Para o regex ser case insensitive, passar o parametro re.I como segundo parametro de re.compile')
    print('Para o regex ser quebrado em varias linhas, por questao de visibilidade, passar o parametro re.VERBOSE como segundo argumento de re.compile')
    print('Somente um argumento é permitido no metodo compile. Para que seja considerado mais de um, utilizar |. Ex re.compile(padrao, re.DOTALL | re.I | re.VERBOSE)')
    print()
    print('O método sub substitui os trechos do texto que combinam com o padrao por um texto definido.')

def subTextRegex():
    # o metodo sub substitui o texto identificado pela regex por outro valor
    nameRegex = re.compile(r'Agent \w+')
    res = nameRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob')
    print(res) # imprime CENSORED gave the secret documents to CENSORED

subTextRegex()

def modoVerbose():
    # para que seja possivel quebrar a regex em varias linhas, para melhor visibilidade
    # passe o argumento VERBOSE
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))? # codigo 3 digitos (\d{3}) ou (|) 3 digitos entre parenteses (\(\d{3}\)) presente ou nao (?)
        (\s|-|\.) # separado por espaco ou ponto ou -
        (\d{3}) # seguido de 3 digitos
        (\s|-|\.) # separado por espaco ou ponto ou -
        \d{4} # seguido de 4 digitos
        (\s*(ext|x|ext.)\s*\d{2,5})? # seguido ou nao por uma extensao (ramal)
    )''', re.VERBOSE) # verbose permite essa quebra de linhas no meio da regex foi usado aspas triplas
    # para passar mais de um argumento para o método compile
    # dessa forma, sera considerado os tres
    phoneRegex = re.compile(r'\w+', re.VERBOSE | re.DOTALL | re.I)