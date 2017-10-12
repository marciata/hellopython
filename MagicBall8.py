import random

# para listas, o python aceita quebras pois identifica que a lista so termina com os colchetes
messages = ["It's certain",
            "It's decidedly so",
            "Yes definitely",
            "Reply hazy try again",
            "Ask again later",
            "Concentrate and ask again",
            "My reply is no",
            "Outlook not so good",
            "Very doubtful"]

print(messages[random.randint(0, len(messages) -1)])

# para quebrar linha em outros comandos q nao sao listas, incluir uma \
print("Exemplo de " + \
    "quebra de linha")