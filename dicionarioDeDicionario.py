allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    # esta iterando sobre os items e atribuindo a chave a variavel k e o valor a variavel v
    for k, v in guests.items():
        # pega a quantidade do item e soma, se nao existir o item, vai retornar 0, sem alterar o dicionario
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples               ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups                 ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes                ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches       ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple pies           ' + str(totalBrought(allGuests, 'apple pies')))
