# ------------------------------------------------------------------------

import random
# import os

vitorias = derrotas = empates = pontuacao = pontuacaoAuxiliar = rodada = 0
questoesJaEscolhidas = []
seDemitiu = False

# ------------------------------------------------------------------------


def criaLinha(frase):

    print('\n' + '\033[30m' + '-' * (len(frase) + 2) + '\033[m' + '\n')

def mostraRegra():

    print('''
    
        Regras:

        ----------------------------------------------------------------------------------------

        - Acertar uma questão sem pedir ajuda       ->      \033[32m+ 3 pontos (Vitória)\033[m
        - Acertar uma questão pedindo ajuda         ->      \033[34m+ 1 ponto (Empate)\033[m
        - Errar uma questão                         ->      \033[33m- 3 pontos (Derrota)\033[m
        - Errar uma questão pedindo ajuda           ->      \033[31m- 6 pontos (Perdeu Confronto direto)\033[m

        ----------------------------------------------------------------------------------------

        ->  102 pontos         -     \033[1;32mCampeão invicto e classificação para a Champions League!!!\033[m
        ->  78 a 100 pontos    -     \033[32mCampeão e Classificação para Champions\033[m
        ->  64 a 77 pontos     -     \033[34mClassificação para a Champions League \033[m
        ->  49 a 63 pontos     -     \033[33mClassificação para a Europa League\033[m
        ->  6 a 34 pontos      -     \033[31mRebaixamento\033[m

        ----------------------------------------------------------------------------------------

        \033[1;31m5 derrotas -> Demitido\033[m

    ''')

def mostraPlacar(resultado):

    if resultado == 'Win':

        while True:

            golsBayern = random.randint(1, 5)
            golsAdversario = random.randint(0, 4)

            if golsBayern >  golsAdversario:

                break

        if golsBayern - golsAdversario == 1:

            print(f'\033[32m{golsBayern} x {golsAdversario}, uma vitória apertada, mas muito importante para a campanha!\033[m')
        
        elif golsBayern - golsAdversario == 2:

            print(f'\033[32m{golsBayern} x {golsAdversario}, uma vitória convincente, importante para aumentar a confiança!\033[m')

        else:

            print(f'\033[32mÉ GOLEADA! Parabéns pelo resultado, um {golsBayern} x {golsAdversario} para comemorar e muito!\033[m')

    elif resultado == 'Lose':
        
        while True:
    
            golsBayern = random.randint(0, 4)
            golsAdversario = random.randint(1, 5)

            if golsBayern <  golsAdversario:

                break

        if  golsAdversario - golsBayern == 1:
    
            print(f'\033[31m{golsAdversario} x {golsBayern}, sabemos que ninguém é imbatível, acontece!\033[m')
        
        elif golsAdversario - golsBayern == 2:

            print(f'\033[31m{golsAdversario} x {golsBayern}, ninguém esperava um resultado desses, trabalhar para melhorar na próxima!\033[m')

        else:

            print(f'\033[31mVEXAME! Esse {golsAdversario} x {golsBayern} deixou a torcida P* da vida, a pressão é grande!\033[m')

    else:

        golsBayern = random.randint(0, 5)
        golsAdversario = golsBayern

        if golsBayern == 0:

            print(f'\033[34mUm {golsBayern} x {golsAdversario} chato... Ambas defesas trabalharam bem!\033[m')

        elif 0 < golsBayern <= 2:

            print(f'\033[34mEmpate ruim! Esse {golsBayern} x {golsAdversario} serviu para notar as falhas no sistema defensivo!\033[m')

        else:

            print(f'\033[34mJOGÃO! Embora não tenhamos conseguido a vitória, esse {golsBayern} x {golsAdversario} foi um espetáculo!\033[m')
# ------------------------------------------------------------------------

#Temos 34 questões, cada uma referente a uma rodada no campeonato
questoes = [

    {'pergunta': 'De quem foi o gol do brasil na histórica goleada aplicada pela alemanha?',
     'options': ['Neymar', 'Oscar', 'Fred', 'Bernard'],
     'resposta': 'Oscar'},

    {'pergunta': 'Quem foi o campeão brasileiro de 2012?',
     'options': ['Corinthians', 'Cruzeiro', 'Fluminense', 'Palmeiras'],
     'resposta': 'Fluminense'},

    {'pergunta': 'Quantos anos o flamengo completou em 2020?',
     'options': ['125', '127', '120', '131'],
     'resposta': '125'},

    {'pergunta': 'Quem deu a assistencia para o primeiro gol de Lionel Messi?',
     'options': ['Eto\'o', 'Ronaldinho Gaúcho', 'Iniesta', 'Deco'],
     'resposta': 'Ronaldinho Gaúcho'},

    {'pergunta': 'Quem é o maior artilheiro da história das copas do mundo?',
     'options': ['Ronaldo Fenômeno', 'Pelé', 'Maradona', 'Klose'],
     'resposta': 'Klose'},

    {'pergunta': 'Antes de ir para o Manchester United da Inglaterra, qual foi o clube de Portugal em que CR7 jogou?',
     'options': ['Porto', 'Boavista', 'Sporting', 'Benfica'],
     'resposta': 'Sporting'},

    {'pergunta': 'Qual é o jogador com mais títulos na história do futebol?',
     'options': ['Iniesta', 'Pelé', 'Zidane', 'Daniel Alves'],
     'resposta': 'Daniel Alves'},

    {'pergunta': 'Qual técnico brasileiro que já foi treinador do Real Madrid?',
     'options': ['Felipão', 'Luxemburgo', 'Mano Menezes', 'Cuca'],
     'resposta': 'Luxemburgo'},

    {'pergunta': 'Qual é o maior artilheiro da seleção brasileira?',
     'options': ['Pelé', 'Neymar', 'Ronaldo', 'Zico'],
     'resposta': 'Pelé'},

    {'pergunta': 'Qual é o time com mais libertadores na história?',
     'options': ['Boca Juniors', 'River Plate', 'Estudiantes', 'Independiente'],
     'resposta': 'Independiente'},

    {'pergunta': 'Dos times abaixos, qual não possui título do mundial de clubes?',
     'options': ['Grêmio', 'Santos', 'Internacional', 'Palmeiras'],
     'resposta': 'Palmeiras'},

    {'pergunta': 'Qual destes clubes possui a terceira maior torcida do Brasil?',
     'options': ['Grêmio', 'Cruzeiro', 'São Paulo', 'Palmeiras'],
     'resposta': 'São Paulo'},

    {'pergunta': '\'La vem o abelão, cheio de paixão, ticatá, ticatá, ticatá\', este vislumbre hino é de um '
                 'torcedor de que clube?',
      'options': ['Internacional', 'Flamengo', 'Fluminense', 'Cruzeiro'],
      'resposta': 'Internacional'},

    {'pergunta': 'A raposa é o mascote de qual dos times abaixo?',
     'options': ['Ceará', 'Botafogo', 'Cruzeiro', 'Atletico Mineiro'],
     'resposta': 'Cruzeiro'},

    {'pergunta': 'Qual destas seleções possui o hino nacional sem letra?',
     'options': ['Chile', 'Espanha', 'Alemanha', 'Itália'],
     'resposta': 'Espanha'},

    {'pergunta': 'Qual foi o último jogador brasileiro a ganhar a bola de ouro?',
     'options': ['Neymar', 'Ronaldo Fenômeno', 'Kaká', 'Zico'],
     'resposta': 'Kaká'},

    {'pergunta': 'Após sair do Milan, qual clube brasileiro contratou Ronaldinho Gaúcho?',
     'options': ['Altético Mineiro', 'Grêmio', 'Fluminense', 'Flamengo'],
     'resposta': 'Flamengo'},

    {'pergunta': 'Qual o goleiro mais caro da história?',
     'options': ['Neuer', 'Oblak', 'Alisson', 'Kepa'],
     'resposta': 'Kepa'},

    {'pergunta': 'Qual o último jogador brasileiro a marcar na final do mundial de clubes?',
     'options': ['Neymar', 'Casemiro', 'Roberto Firmino', 'Marcelo'],
     'resposta': 'Roberto Firmino'},

    {'pergunta': 'Abaixo temos 3 times e uma seleção. Qual deles é a seleção',
     'options': ['Real Madrid', 'Barcelona', 'Flamengo', 'Bayern De Munique'],
     'resposta': 'Flamengo'},

    {'pergunta': 'O título de \'Imperador\' é designado a qual dos jogadores abaixo?',
     'options': ['Roberto Carlos', 'Adriano', 'Ronaldinho Gaúcho', 'Ronaldo Fenômeno'],
     'resposta': 'Adriano'},

    {'pergunta': 'Qual dos jogadores abaixo é brasileiro naturalizado italiano?',
     'options': ['Thiago Alcântara', 'Jorginho', 'Rafinha', 'Diego Costa'],
     'resposta': 'Jorginho'},

    {'pergunta': 'Dos times abaixo, qual foi o campeão da Copa do Brasil de 2018?',
     'options': ['Cruzeiro', 'Corinthians', 'Palmeiras', 'Grêmio'],
     'resposta': 'Cruzeiro'},

    {'pergunta': 'Qual o autor da tracionalíssima frase \'Fala zezé, bom dia cara!\'?',
     'options': ['Edilson', 'Thiago Neves', 'Fred', 'Gabigol'],
     'resposta': 'Thiago Neves'},

    {'pergunta': 'Qual foi o último brasileiro a ganhar o prêmio Puskás?',
     'options': ['Neymar', 'Wendel Lira', 'Ronaldinho Gaúcho', 'Coutinho'],
     'resposta': 'Wendel Lira'},

    {'pergunta': 'Qual jogador foi responsável por fazer o gol da Alemanha na final da Copa do Mundo de 2014?',
     'options': ['Kedhira', 'Muller', 'Schrurrle', 'Mario Gotze'],
     'resposta': 'Mario Gotze'},

    {'pergunta': 'Qual o time italiano com mais Champions League conquistadas?',
     'options': ['Milan', 'Juventus', 'Internazionale', 'Roma'],
     'resposta': 'Milan'},

    {'pergunta': 'Na copa de 2010, qual seleção eliminou o Brasil?',
     'options': ['Espanha', 'Alemanha', 'Uruguai', 'Holanda'],
     'resposta': 'Holanda'},

    {'pergunta': 'Qual o técnico com mais títulos na história do futebol?',
     'options': ['Felipão', 'Guardiola', 'Mourinho', 'Alex Ferguson'],
     'resposta': 'Alex Ferguson'},

    {'pergunta': 'Qual é o time com mais rebaixamentos da história do brasileirão?',
     'options': ['Vasco', 'Botafogo', 'Avaí', 'América-Mg'],
     'resposta': 'América-Mg'},

    {'pergunta': 'Qual dos clubes abaixo não possui libertadores?',
     'options': ['Vasco', 'Cruzeiro', 'Fluminense', 'Internacional'],
     'resposta': 'Fluminense'},

    {'pergunta': 'Qual foi a contratação mais cara da história?',
     'options': ['Neymar-PSG', 'Neymar-BAR', 'CR7 - JUVE', 'Griezmann-BAR'],
     'resposta': 'Neymar-PSG'},

    {'pergunta': 'Quem bateu o último penalti do Palmeiras na decisão da CDB de 2015?',
     'options': ['Gabriel Jesus', 'Fernando Prass', 'Dudu', 'Vitor Hugo'],
     'resposta': 'Fernando Prass'},

     {'pergunta': 'Quem foi o técnico da seleção brasileira na conquista do tetra?',
      'options': ['Zagalo', 'Dunga', 'Parreira', 'Felipão'],
      'resposta': 'Parreira'}
]

# Programa Principal!!!
# -------------------------------------------------------------------------

print( '\033[1;33mSeja muito bem vindo!\033[m\n' + '\n'+' ' * 3 + 'O jogo é baseado em responder perguntas, onde cada uma delas representa uma rodada do campeonato alemão. Você é o técnico do Bayern, e tem a missão de ganhar mais um título desta competição para o clube. \n')

print(' ' * 3 + 'Você foi contratado para ser o técnico do maior time da Alemanha, o todo poderoso Bayern de Munique. A diretoria está bem confiante no seu trabalho, e acredita que você tem um grande potencial para fazer o time campeão nesta temporada. O orçamento da equipe é disparado o maior do país, sendo o título do campeonato alemão  mais que obrigação. Nas ultimas 5 temporadas, o Bayern não perdeu mais que 4 vezes durante todo o campeonato, logo, se você perder 5 vezes você será demitido. \n')

mostraRegra()

# ---------------------------------------------------------------------------------------------------------

# Validando entrada

while True:
    
    start = input('Digite Sim quando estiver pronto para encarar esse desafio! \n').upper().strip()[0]

    if start not in 'S':

        print('\033[31mDigite uma opção válida!\033[m')
    
    else: 

        break

# ---------------------------------------------------------------------------------------------------------

while True:

    rodada += 1

    pediuAjuda = False
    
    #Verificando se a pergunta já foi feita anteriormente

    while True:

        questaoEscolhida = random.randint(0, len(questoes) - 1)

        if questaoEscolhida not in questoesJaEscolhidas:

            break

        else:

            continue
    

    questoesJaEscolhidas.append(questaoEscolhida)


    # -------------------------------------------------------------------------
    # Vai embaralhar as opções
    # -------------------------------------------------------------------------

    random.shuffle(questoes[questaoEscolhida]['options'])

    # -------------------------------------------------------------------------------------
    
    while True:

        if pediuAjuda == True:
            
            criaLinha(questoes[questaoEscolhida]['pergunta'])
            print('\033[31m!!!\033[m A alternativa marcada de vermelho é uma das erradas \033[31m!!!\033[m')

        # Vai mostrar a rodada

        criaLinha(questoes[questaoEscolhida]['pergunta'])
        print(f'\033[1;36m{rodada}º Rodada\033[m')
        criaLinha(questoes[questaoEscolhida]['pergunta'])

        # Vai mostrar a pergunta
        print('\033[33m'+questoes[questaoEscolhida]['pergunta'] + '\033[m')
        criaLinha(questoes[questaoEscolhida]['pergunta'])

        if pediuAjuda == False:

            # Vai por as opções na tela
            
            for num, option in enumerate(questoes[questaoEscolhida]['options']):
        
                print(f'[ {num + 1} ] {option}')

        else:

            for num, option in enumerate(questoes[questaoEscolhida]['options']):

                # Vai por as opções na tela

                try:

                    if num == opcaoErradaRetirada:

                        print(f'\033[31m[ {num + 1} ] {option}\033[m')

                    else:

                        print(f'[ {num + 1} ] {option}')

                except:

                    pass

        criaLinha(questoes[questaoEscolhida]['pergunta'])

        print('[ 5 ] AJUDA')
        print('[ 6 ] SITUAÇÃO')
        print('[ 7 ] SAIR')
        print('[ 8 ] REGRAS')

        criaLinha(questoes[questaoEscolhida]['pergunta'])

        # ------------------------------------------------------------------------------------

        # Validando apenas valores entre 1 e 8 do tipo int

        while True:

            try:

                while True:

                    opcaoEscolhida = int(input('\033[33mSua opção: \033[m'))

                    if opcaoEscolhida < 1 or opcaoEscolhida > 8:

                        print('Digite um número entre 1 e 8')
                        continue

                    else:

                        break


            except(ValueError, TypeError):

                print('Informe apenas números que correspondam às opções.')

                continue

            else:

                break

        criaLinha(questoes[questaoEscolhida]['pergunta'])

        # -----------------------------------------------------------------------------------------------------

        # Se o usuario digitou a opção de ajuda

        if opcaoEscolhida == 5:


            # 
            
            print('O sistema de ajuda mostrará uma alternativa errada com a cor vermelha, aumentando assim suas possibilidades de acerto\n')


            while True:

                r = input(f'Você tem certeza que quer ajuda?\033[1;31m Você perderá 2 pontos! [S/N]\033[m \n').upper().strip()[0]

                criaLinha(questoes[questaoEscolhida]['pergunta'])

                if r in 'SN':
                    break

                print('ERRO! Responda apenas S ou N.')
                criaLinha(questoes[questaoEscolhida]['pergunta'])

            # ---------------------------------------------------------------------------------------------    

            # Se ele confirmou que quer ajuda

            if r == 'S':

                #Se o usuario ja tiver pedido ajuda na questao

                if pediuAjuda == True:
                    
                    # os.system('clear')
                    print('Você Já pediu ajuda nessa questão!')
                    continue

                else:

                    opcoesComAjuda = questoes[questaoEscolhida]['options'].copy()

                    respostaCerta = opcoesComAjuda.index(questoes[questaoEscolhida]['resposta'])

                    while True:

                        # Loop para escolher uma opção errada

                        opcaoErradaRetirada = random.randint(0, 3)

                        if opcaoErradaRetirada != respostaCerta:

                            pontuacao -= 2
                            pediuAjuda = True
                            break
                    
                    continue
            else:

                continue

        # -----------------------------------------------------------------------------------------------------

        if opcaoEscolhida == 6:

            rodadasRestante = 34 - rodada

            # Se a pontuação for menor que 0, não é conviniente mostrar ao usuário, pois pontuação negativa serve apenas para a lógica do programa, no mundo real, não é possivel um time pontuar -6, por exemplo

            if pontuacao <= 0:

                # Aqui estou substituindo o valor negativo da pontuacao por 0, e assim guardando o valor da pontuação em outra variavel, para que assim possa ter essa pontuação de volta no final da iteração

                pontuacaoAuxiliar = pontuacao
                pontuacao = 0

            print(f'\033[1mVitórias:\033[m \033[32m{vitorias}\033[m')
            print(f'\033[1mEmpates:\033[m \033[34m{empates}\033[m')
            print(f'\033[1mDerrotas:\033[m \033[31m{derrotas}\033[m')
            print(f'\033[1mPontos:\033[m \033[33m{pontuacao}\033[m')
            print(f'\033[1mRodadas Restante:\033[m \033[36m{rodadasRestante}\033[m')

            criaLinha(questoes[questaoEscolhida]['pergunta'])

            print('[ 7 ] SAIR')
            print('[ 8 ] REGRAS')
            print('[ 9 ] Voltar')

            # Aqui estou retomando o valor anterior da variavel pontuacao, e 'limpando' o valor da variável pontuacao auxiliar para próximas iterações
  
            if pontuacaoAuxiliar < 0:

                pontuacao = pontuacaoAuxiliar
                pontuacaoAuxiliar = 0


            criaLinha(questoes[questaoEscolhida]['pergunta'])

            # Validação de resposta
            while True:
    
                try:

                    while True:

                        opcaoEscolhida = int(input())

                        if opcaoEscolhida < 7 or opcaoEscolhida > 9:

                            print('Informe uma opção válida!')
                            continue

                        else:

                            break


                except(ValueError, TypeError):

                    print('Informe apenas números que correspondam às opções.')

                    continue

                else:

                    break
            
            if opcaoEscolhida == 9:
            
                continue

        if opcaoEscolhida == 7:

            while True:

                sair = input(f'Tem certeza que deseja se demitir e assim acabar o jogo? [S/N] \n').strip().upper()[0]

                if sair in 'SN':

                    break

                print('ERRO! Responda apenas S ou N.')
                criaLinha(questoes[questaoEscolhida]['pergunta'])

            if sair == 'S':

                seDemitiu = True            
                break

            else:

                continue

        if opcaoEscolhida == 8:

            mostraRegra()

            while True:

                criaLinha(questoes[questaoEscolhida]['pergunta'])

                voltar = input('Digite \033[32mS\033[m para voltar: ').upper().strip()[0]
                
                if voltar in 'S':

                    break
                
                criaLinha(questoes[questaoEscolhida]['pergunta'])
                print('Digite uma opção válida!')
                    

            continue

        # Se a resposta for certa
        
        if questoes[questaoEscolhida]['options'][opcaoEscolhida - 1] == questoes[questaoEscolhida]['resposta']:

            # os.system('clear')

            if pediuAjuda == True:

                empates += 1
                resultadoPartida = 'Draw'
                print(f'\033[34mReposta certa\033[m')

            else:

                resultadoPartida = 'Win'
                print(f'\033[32mReposta certa!\033[m')

            pontuacao += 3
            vitorias += 1
            

            mostraPlacar(resultadoPartida)

            break
    
        # Se a resposta for errada
        else: 
            
            # os.system('clear')

            # Se o usuario ja tiver pedido ajuda, logo ele perdeu um confronto direto
            # portanto, num confronto direto ele deve perder 6 pontos, como está nas regras
            # -2 da ajuda -4 da derrota = -6
          
            resultadoPartida = 'Lose'

            if pediuAjuda == True:
                
                pontuacao -= 4
                print('\033[31mVocê perdeu um confronto direto, a torcida cobra por resultados melhores!\033[m')
            
            # Se ele nao tiver pedido ajuda, simplesmente vai perder 3 pontos, pois foi uma derrota
            
            else:
            
                pontuacao -= 3
                print('\033[31mResposta Errada!\033[m')
            
            mostraPlacar(resultadoPartida)

            derrotas += 1
            
            break

        # -----------------------------------------------------------------------------------------------------


    if derrotas == 5:

        print('-------------------------------------------------------------------------------\n')

        print('Você perdeu 5 jogos no comando da equipe, e o combinado no contrato foi que se você perdesse mais de 4 vezes seu trabalho no clube seria encerrado. Infelizmente as coisas assim aconteceram, e viemos notificá-lo da sua demissão e de toda sua  comissão técnica. O Bayern de Munique agradece os serviços prestados e lhe deseja boa sorte nos próximos trabalhos.')
    
        break

    #Acabaram as perguntas, ou seja, o usuário conseguiu não ser demitido até o fim do campeonato

    elif (len(questoesJaEscolhidas) == len(questoes)):

            
    # Verificando situação do bayern no campeonato

        print('-------------------------------------------------------------------------------\n')

        if vitorias == 34:

            print('\033[32mCAAARACAAA!!! Isso que é campanha! A torcida está louca com a campanha do time!')
            print('Nenhum time na história da bundesliga conseguiu 100\% de aproveitamento dos pontos, você foi incrível!')
            print('Parabéns Pelo título, você entrou para a história não só do clube, como também do campeonato!\033[m')
        
        elif 78 <= pontuacao <= 100:

            print('\033[32mParabéns pela campanha! Você atingiu todas nossas expectativas e da torcida!')
            print('Bora comemorar esse título porque essa torcida merece!!!\033[m')
        
        elif 64 <= pontuacao <= 77:

            print('\033[36mParábens pela classificação para a Champions, mas a diretoria entrou em um consenso e não desejamos contar com seu trabalho na próxima temporada. Embora a campanha tenha sido razoável, o Bayern não é um time que se contenta com pouco. Desejamos todo o sucesso do mundo para você, e agradecemos aos serviços prestados.\033[m')

        elif 49 <= pontuacao <= 63:

            print('\033[33mAgradecemos ao serviços prestados, mas não contamos com seu trabalho para a próxima temporada. Um clube como o Bayern de Munique não pode ficar de fora da champions. Boa sorte nos próximos trabalhos.\033m')

        elif 6 <= pontuacao <= 36:

            print('\033[31mÉ inadimiscível um clube com um orçamento tão alto como o nosso ser rebaixado na Bundesliga. Você e toda sua comissão técnica a partir de hoje não comanda mais o time principal do clube. Agradecemos aos serviços prestados e desejamos sorte na sua carreira.\033[m')

        else:
            
            print('\033[033mPara um clube como o Bayern de Munique é inadimiscível ficar no meio de tabela, agradecemos o trabalho mas voce e toda sua comissão técnica a partir de hoje não trabalha mais no clube.\033m')


        break


    if seDemitiu == True:

        print('Boa sorte na sua jornada, esperamos que tenha sucesso!')
        break

    continue


# aproveitamento = round(((((vitorias * 3) + (1 * empates)) / (3 * rodada)) * 100), 2)

# Se a pontuação for menor que 0, não é conviniente mostrar ao usuário, pois pontuação negativa serve apenas para a lógica do programa, no mundo real, não é possivel um time pontuar -6, por exemplo

if pontuacao <= 0:

    # Aqui estou substituindo o valor negativo da pontuacao por 0, e assim guardando o valor da pontuação em outra variavel, para que assim possa ter essa pontuação de volta no final da iteração

    pontuacaoAuxiliar = pontuacao
    pontuacao = 0

print(f'''
-------------------------------------------------------------------------------

Vitórias: \033[32m{vitorias}\033[m
Derrotas:  \033[31m{derrotas}\033[m
Empates: \033[34m{empates}\033[m

-------------------------------------------------------------------------------

''')

# Aqui estou retomando o valor anterior da variavel pontuacao

# if pontuacaoAuxiliar < 0:

#     pontuacao = pontuacaoAuxiliar
 
