# Encontra numeros de telefone e enderecos de email a partir do clipboard
import pyperclip, re

# Expressao regular para identificar telefones
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # codigo 3 digitos (\d{3}) ou (|) 3 digitos entre parenteses (\(\d{3}\)) presente ou nao (?)
    (\s|-|\.) # separado por espaco ou ponto ou -
    (\d{3}) # seguido de 3 digitos
    (\s|-|\.) # separado por espaco ou ponto ou -
    (\d{4}) # seguido de 4 digitos
    (\s*(ext|x|ext.)\s*\d{2,5})? # seguido ou nao por uma extensao (ramal)
)''', re.VERBOSE)  # verbose permite essa quebra de linhas no meio da regex foi usado aspas triplas

# Expressao regular para identificar email
emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+) # conjunto de letras minusculos ou maiusculos, ., -, %, + ou -. Dentro de colchetes nao precisa escapar  
                        (@) # seguido de arroba
                        ([a-zA-Z0-9.-]+) # nome do dominio
                        (\.[a-zA-Z]{2,4}) # ponto seguido de outros caracteres
                        ''', re.VERBOSE)

# Pega o conteudo do clipboard
text = str(pyperclip.paste())

matches = []
# Procura telefones no texto e joga na lista matches
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) # padroniza para ddd-numero inicio-numero fim
    if (groups[6]) != '':
        phoneNum += ' x' + groups[6] # se tiver extensao, inclui espaco x e a extensao
    print('encontrado', groups)
    print('appended', phoneNum)
    matches.append(phoneNum)

# Procura emails no texto e joga na lista matches
for groups in emailRegex.findall(text):
    matches.append(''.join(groups))
    print('Encontrado ', groups)

# copia o resultado para o clipboard
if (len(matches) > 0):
    saida = '\n'.join(matches)
    pyperclip.copy(saida)
    print('Copied to clipboard')
    print(saida)
else:
    print('No phone numbers or email addresses found.')
