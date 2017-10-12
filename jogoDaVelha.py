def printBoard(board):
    print(board['top-l'] + "|" + board['top-m'] + "|" + board['top-r'])
    print("=+=+=")
    print(board['mid-l'] + "|" + board['mid-m'] + "|" + board['mid-r'])
    print("=+=+=")
    print(board['bottom-l'] + "|" + board['bottom-m'] + "|" + board['bottom-r'])

def instructions():
    print('Bem vindo ao jogo da velha')
    print('Para jogar, informe: ')
    print('top-l para primeira fileira a esquerda, top-m para primeira fileira meio e top-r para primeira fileira direita')
    print('mid-l para segunda fileira a esquerda, mid-m para segunda fileira meio e mid-r para segunda fileira direita')
    print('bottom-l para terceira fileira a esquerda, bottom-m para terceira fileira meio e bottom-r para terceira fileira direita')

theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'bottom-l': ' ', 'bottom-m': ' ', 'bottom-r': ' '}

instructions()
print()
turn = 'X'
jogada = 0

while jogada < 9:
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on whicht space?')
    move = input()
    try:
        if (theBoard[move] != ' '):
            print('Esse espaco já esta preenchido')
            continue
    except KeyError:
        print('Valor invalido')
        continue;

    theBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    jogada += 1

printBoard(theBoard)

