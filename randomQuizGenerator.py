import random

# um dicionario normal
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississipi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', ' New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Winsconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# para gerar 35 provas diferentes
for quizNum in range(35):
    # criando um arquivo com um nome unico e com permissao de escrita
    quizFile = open('capitalsquiz%s.txt' %(quizNum + 1), 'w')
    # criando outro arquivo para guardar o gabarito dessa prova
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # escrevendo um cabecalho no arquivo para preencher nome, data e periodo
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    # escrevendo 20 espacos e o titulo da prova
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Forms %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    # Embaralha a ordem dos estados
    random.shuffle(states)

    # 50 questoes na prova
    for questionNum in range(50):
        # Obtém respostas corretas e incorretas
        # busca a resposta correta
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        # deleta a resposta correta da lista de respostas
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # pega 3 itens aleatorios da lista de respostas possíveis
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        # embaralha a lista de respostas para que a correta nao seja sempre a ultima
        random.shuffle(answerOptions)

        # Grava a pergunta e as opções de resposta no arquivo de prova
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))

        for i in range(4):
            # 'ABCD' é um array, e cada iteracao pegara um dos elementos desse array
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Grava o gabarito com as respostas em um arquivo
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()