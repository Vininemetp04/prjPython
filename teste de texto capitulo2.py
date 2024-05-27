#RAINHAS DAS BRUXAS
import random
import funcs as FN 

def decidir_acompanhamento_aria():
    """
    Função para decidir se Aria acompanhará o jogador na jornada.
    """
    global aria_acompanhando
    FN.write("", "\nVocê gostaria que Aria acompanhasse você na jornada?\n")
    FN.write("", "1. Sim, Aria deve vir conosco.\n")
    FN.write("", "2. Não, Aria deve ficar no reino.\n")
    
    escolha_acompanhamento = escolha()

    if escolha_acompanhamento == '1':
        FN.write("Aria", "\n'Aria: Eu irei com vocês e usarei minhas habilidades para proteger nosso grupo contra inimigos à distância.'")
        aria_acompanhando = True
        # Aria acompanha o grupo
    elif escolha_acompanhamento == '2':
        FN.write("Aria", "\n'Aria: Entendo. Boa sorte em sua jornada. Que os deuses estejam com vocês.'")
        aria_acompanhando = False
        # Aria fica no reino
    else:
        FN.write("", "\nEscolha inválida. Aria ficará no reino por padrão.")
        aria_acompanhando = False
        # Aria fica no reino por padrão

# Chamar a função para a decisão de acompanhamento de Aria após as escolhas iniciais
decidir_acompanhamento_aria()

# Continuar a história com o encontro da Rainha das Bruxas
encontro_com_rainha_bruxa()

def encontro_com_rainha_bruxa():
    """
    Função para simular o encontro com a Rainha das Bruxas.
    """
    FN.write("", "\nVocê e Merlim chegam à morada da Rainha das Bruxas. A atmosfera é sombria e cheia de mistério.\n")
    FN.write("", "De repente, vocês são surpreendidos por um grupo de Ratos Mutantes que atacam ferozmente!\n")

    FN.write("", "Escolha sua ação:\n")
    FN.write("", "1. Utilizar um feitiço de Merlim\n")
    FN.write("", "2. Se esconder atrás dos barris\n")
    
    if aria_acompanhando:
        FN.write("", "3. Colocar Aria para atirar nos ratos\n")
    else:
        FN.write("", "3. Tentar distrair os ratos\n")

    escolha_ratos = obter_escolha_opcao()

    if escolha_ratos == '1':
        FN.write("", "\nMerlim lança um feitiço poderoso, mas algo dá errado e o feitiço se volta contra vocês!")
        FN.write("", "Você e Merlim sofreram dano! Perderam 20 HP cada.")
        # Subtrair HP do jogador e de Merlim
    elif escolha_ratos == '2':
        FN.write("", "\nVocês se escondem atrás dos barris, evitando o ataque dos ratos. Após algum tempo, os ratos vão embora.")
        # Jogador evita dano, mas perde tempo
    elif escolha_ratos == '3':
        if aria_acompanhando:
            FN.write("", "\nAria rapidamente pega seu arco e dispara flechas certeiras, derrotando os ratos mutantes!")
            FN.write("", "Vocês venceram a batalha sem sofrer danos.")
            # Jogador vence sem sofrer danos
        else:
            sucesso = random.choice([True, False])
            if sucesso:
                FN.write("", "\nVocê distrai os ratos com sucesso, permitindo que você e Merlim escapem sem serem feridos.")
                # Jogador escapa sem sofrer danos
            else:
                FN.write("", "\nSua tentativa de distrair os ratos falha, e vocês são atacados!")
                FN.write("", "Você e Merlim sofreram dano! Perderam 15 HP cada.")
                # Subtrair HP do jogador e de Merlim
    else:
        FN.write("", "\nEscolha inválida. Os ratos atacam vocês durante a hesitação.")
        FN.write("", "Você e Merlim sofreram dano! Perderam 25 HP cada.")
        # Subtrair mais HP do jogador e de Merlim

def encontro_com_rainha_bruxa():
    """
    Função para simular o encontro com a Rainha das Bruxas.
    """
    FN.write("", "\nVocês entram no palácio sombrio da Rainha das Bruxas. Ela os recebe com um sorriso sinistro.\n")
    FN.write("Rainha das Bruxas", "'Vocês devem ser os guerreiros corajosos que vieram ao meu castelo pedir ajuda. Bom primeiro vocês devem me responder um enigma e talvez após isso, eu os ajudarei.'\n")
    
    # Enigma e opções
    enigma = "Qual é o próximo número na sequência: 1, 1, 2, 3, 5, 8, _?"
    opcao1 = "A) 9"
    opcao2 = "B) 10"
    opcao3 = "C) 13"

    FN.write("", enigma)
    FN.write("", opcao1)
    FN.write("", opcao2)
    FN.write("", opcao3)

    # Escolha do jogador
    resposta_enigma = FN.escolha()

    if resposta_enigma == 'A':
        FN.write("Rainha das Bruxas", "\n'Errado! Preparem-se para sofrer as consequências.'")
        FN.write("", "Você e Merlim sofrem dano! Perderam 15 HP cada.")
        # Subtrair HP do jogador e de Merlim
    elif resposta_enigma == 'B':
        FN.write("Rainha das Bruxas", "\n'Errado! Preparem-se para sofrer as consequências.'")
        FN.write("", "Você e Merlim sofrem dano! Perderam 15 HP cada.")
        # Subtrair HP do jogador e de Merlim
    elif resposta_enigma == 'C':
        FN.write("Rainha das Bruxas", "\n'Correto! Vocês têm inteligência. Como prometido, aqui está minha ajuda.'")
        FN.write("", "Você e Merlim ganham a ajuda da Rainha das Bruxas e 50 pontos de experiência!")
        # Adicionar ajuda da Rainha e experiência ao jogador
    else:
        FN.write("", "\nEscolha inválida. A Rainha das Bruxas fica irritada e ataca vocês!")
        FN.write("", "Você e Merlim sofrem dano! Perderam 20 HP cada.")
        # Subtrair HP do jogador e de Merlim
        FN.write("", "Bom, eu sei que alguém muito próximo do Rei resolveu o tirar de vista devido a um plano ligeiramente horrível.",)
FN.write("Rainha das Bruxas", "Eu poderia fazer melhor",)
FN.write("Rainha das Bruxas", "Ela solta uma risada. 'Bom, para que vocês consigam o que desejam, devem ir até a Floresta do Silêncio,")
FN.write("Rainha das Bruxas", "lá encontrarão uma de minhas guardiãs e ela estará com o mapa até a caverna do Dragão das Trevas.'")

def encontrar_driade():
    FN.write("Narrador", "Os personagens continuam pela trilha da Lua Crescente, seguindo as instruções da Driade.")
    FN.write("Narrador", "Após algum tempo, eles se deparam com uma criatura majestosa, a Driade.")
    FN.write("Driade", "'Quem ousa pisar em meus frutos?'")
    FN.write("Narrador", "Os personagens ficam em silêncio, cautelosos.")
    FN.write("Driade", "'Eu os escuto, como escuto tudo que ocorre em minha floresta.'")
    resposta = input("Merlim: 'Nos perdoe, estamos em busca de uma feiticeira, Lyra, que vive aqui na floresta. Qual o motivo de sua busca?' ")

    if "ajuda" in resposta or "perigo" in resposta:
        FN.write("Driade", "'Seus motivos parecem sinceros. Sigam para o sul até o Vale Esmeralda. Lá encontrarão Lyra.'")
    elif "equilíbrio" in resposta or "natureza" in resposta:
        FN.write("Driade", "'Sigam pela trilha das estrelas à leste. Ela os aguardará na Clareira das Águas Tranquilas.'")
    else:
        FN.write("Driade", "'Seus corações parecem puros, mas o caminho até Lyra é perigoso. Siga a trilha da Lua Crescente ao oeste.'")

    def encontrar_lyra():
    """
    Função para simular o encontro com Lyra, a guardiã da floresta.
    """
    FN.write("", "Vocês seguem o caminho e encontram Lyra, a guardiã da floresta.")
    FN.write("Lyra", "'Sou Lyra, um passarinho verde me contou que alguns jovens estavam atrás de mim, o que desejam?'")
    
    # Opções do jogador
    opcao1 = "A) Encontrar o Rei."
    opcao2 = "B) Somos apenas meros servos da Rainha Bruxa."
    opcao3 = "C) Queremos um combate."

    FN.write("", opcao1)
    FN.write("", opcao2)
    FN.write("", opcao3)

    # Escolha do jogador
    escolha = input("Escolha uma opção (A, B ou C): ")

    if escolha == 'A':
        FN.write("Lyra", "'Lamento, mas não posso ajudá-los nesse assunto.'")
        FN.write("", "Lyra desaparece diante de vocês, deixando-os sem ajuda.")
    elif escolha == 'B':
        FN.write("Lyra", "'Vejo que vocês têm boas intenções. Aqui está o mapa até a caverna dos Ladrões.'")
        player.xp += 10  # Ganha 10 XP
        FN.write("", "Vocês ganham o mapa e 10 pontos de experiência!")
    elif escolha == 'C':
        FN.write("Lyra", "'Se é um combate que desejam, assim seja.'")
        iniciar_combate_lyra()

def iniciar_combate_lyra():
    FN.write("", "Você decide entrar em combate com Lyra.")
    FN.write("Lyra", "'Preparem-se para enfrentar minha magia!'")
    
    # Opções de combate
    opcao1 = "A) Atacar Lyra."
    opcao2 = "B) Merlim interrompe."
    opcao3 = "C) Fugir."

    FN.write("", opcao1)
    FN.write("", opcao2)
    FN.write("", opcao3)

    # Escolha do jogador
    escolha_combate = input("Escolha uma opção (A, B ou C): ")

    if escolha_combate == 'A':
        player.hp -= 20  # Perde 20 HP
        FN.write("", "Você ataca Lyra e sofre dano!")
        if player.hp <= 0:
            FN.write("", "Seu HP está baixo, beba a poção de cura!")
    elif escolha_combate == 'B':
        FN.write("Merlim", "'Pare com isso, Lyra! Não precisamos lutar.'")
        player.xp += 10  # Ganha 10 XP
        FN.write("", "Merlim interrompe o combate e vocês ganham 10 pontos de experiência!")
    elif escolha_combate == 'C':
        FN.write("", "Você decide fugir do combate.")
        FN.write("", "Lyra deixa vocês partirem, mas com uma advertência.")