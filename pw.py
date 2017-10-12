# um programa para repositorio de senhas que nao é seguro
# uso: informe o que deseja acessar (ex email) e a senha sera copiada para o clipboard
PASSWORDS = {'email': 'senhadoemail',
             'blog': 'senhadoblog',
             'luggage': '12345'}

import sys, pyperclip
if (len(sys.argv) < 2):
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # o primeiro argumento da linha de comando é o nome do arquivo

if (account in PASSWORDS):
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)