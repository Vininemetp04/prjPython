#RAINHAS DAS BRUXAS
import random
import funcs as FN 
import menu as MN

def decidir_acompanhamento_aria(pl):
    """
    Função para decidir se Aria acompanhará o jogador na jornada.
    """
    global aria_acompanhando
    opeMenu = ["Sim, Aria deve vir conosco.", "Não, Aria deve ficar no reino."]
    
    menu = MN.menu(opeMenu, 2, 2, "Você gostaria que Aria acompanhasse você na jornada?")
    menu.draw(0)
    menu.wait()
    escolha_acompanhamento = menu.ans
    menu.close()

    match escolha_acompanhamento:
        case 0:
            FN.write("Aria", "Aria: Eu irei com vocês e usarei minhas habilidades para proteger nosso grupo contra inimigos à distância.")
            aria_acompanhando = True
            # Aria acompanha o grupo
        case 1:
            FN.write("Aria", "Aria: Entendo. Boa sorte em sua jornada. Que os Narradores estejam com vocês.")
            aria_acompanhando = False
            # Aria fica no reino
    pl.parte = 2
    pl.save()
    encontro_com_rainha_bruxa(pl)

def encontro_com_rainha_bruxa(pl):
    """
    Função para simular o encontro com a Rainha das Bruxas.
    """
    FN.write("", "Você e Merlim chegam à morada da Rainha das Bruxas. A atmosfera é sombria e cheia de mistério.")
    FN.write("", "De repente, vocês são surpreendidos por um grupo de Ratos Mutantes que atacam ferozmente!")
    
    opeMenu = ["Utilizar um feitiço de Merlim", "Se esconder atrás dos barris"]

    if aria_acompanhando:
        opeMenu.append("Colocar Aria para atirar nos ratos")
    else:
        opeMenu.append("Tentar distrair os ratos")
        
    menu = MN.menu(opeMenu, 2, 2, "Escolha sua ação:")
    menu.draw(0)
    menu.wait()
    escolha_ratos = menu.ans
    menu.close()

    if escolha_ratos == 0:
        FN.write("", "Merlim lança um feitiço poderoso, mas algo dá errado e o feitiço se volta contra vocês!")
        FN.write("", "Você e Merlim sofreram dano! Perderam 20 HP cada.")
        pl.hp -= 20
        # Subtrair HP do jogador e de Merlim
    elif escolha_ratos == 1:
        FN.write("", "Vocês se escondem atrás dos barris, evitando o ataque dos ratos. Após algum tempo, os ratos vão embora.")
        # Jogador evita dano, mas perde tempo
    elif escolha_ratos == 2:
        if aria_acompanhando:
            FN.write("", "Aria rapidamente pega seu arco e dispara flechas certeiras, derrotando os ratos mutantes!")
            FN.write("", "Vocês venceram a batalha sem sofrer danos.")
            # Jogador vence sem sofrer danos
        else:
            sucesso = random.choice([True, False])
            if sucesso:
                FN.write("", "Você distrai os ratos com sucesso, permitindo que você e Merlim escapem sem serem feridos.")
                # Jogador escapa sem sofrer danos
            else:
                FN.write("", "Sua tentativa de distrair os ratos falha, e vocês são atacados!")
                FN.write("", "Você e Merlim sofreram dano! Perderam 15 HP cada.")
                pl.hp -= 15
                # Subtrair HP do jogador e de Merlim
    pl.parte = 3
    pl.save()
    encontro_com_rainha_bruxa2(pl)

def encontro_com_rainha_bruxa2(pl):
    """
    Função para simular o encontro com a Rainha das Bruxas.
    """
    FN.write("", "Vocês entram no palácio sombrio da Rainha das Bruxas. Ela os recebe com um sorriso sinistro.")
    FN.write("Rainha das Bruxas", "Vocês devem ser os guerreiros corajosos que vieram ao meu castelo pedir ajuda. Bom primeiro vocês devem me responder um enigma e talvez após isso, eu os ajudarei.")
    
    # Enigma e opções
    ope = ["9", "10", "13"]
    title = "Qual é o próximo número na sequência: 1, 1, 2, 3, 5, 8, _?"
    menu = MN.menu(ope, 2, 2, title)
    menu.draw(0)
    menu.wait()
    resposta_enigma = menu.ans
    menu.close()

    if resposta_enigma == 0:
        FN.write("Rainha das Bruxas", "Errado! Preparem-se para sofrer as consequências.")
        FN.write("", "Você e Merlim sofrem dano! Perderam 15 HP cada.")
        pl.hp -= 15
        # Subtrair HP do jogador e de Merlim
    elif resposta_enigma == 1:
        FN.write("Rainha das Bruxas", "Errado! Preparem-se para sofrer as consequências.")
        FN.write("", "Você e Merlim sofrem dano! Perderam 15 HP cada.")
        pl.hp -= 15
        # Subtrair HP do jogador e de Merlim
    elif resposta_enigma == 3:
        FN.write("Rainha das Bruxas", "Correto! Vocês têm inteligência. Como prometido, aqui está minha ajuda.")
        FN.write("", "Você e Merlim ganham a ajuda da Rainha das Bruxas e 50 pontos de experiência!")
        # Adicionar ajuda da Rainha e experiência ao jogador
    FN.write("Rainha das Bruxas", "Eu poderia fazer melhor",)
    FN.write("Rainha das Bruxas", "Ela solta uma risada. Bom, para que vocês consigam o que desejam, devem ir até a Floresta do Silêncio,")
    FN.write("Rainha das Bruxas", "lá encontrarão uma de minhas guardiãs e ela estará com o mapa até a caverna do Dragão das Trevas.")
    pl.parte = 4
    pl.save()
    encontrar_driade(pl)

def encontrar_driade(pl):
    FN.write("Narrador", "Os personagens continuam pela trilha da Lua Crescente, seguindo as instruções da Driade.")
    FN.write("Narrador", "Após algum tempo, eles se deparam com uma criatura majestosa, a Driade.")
    FN.write("Driade", "Quem ousa pisar em meus frutos?")
    FN.write("Narrador", "Os personagens ficam em silêncio, cautelosos.")
    FN.write("Driade", "Eu os escuto, como escuto tudo que ocorre em minha floresta.")
    resposta = input("Merlim: Nos perdoe, estamos em busca de uma feiticeira, Lyra, que vive aqui na floresta. Qual o motivo de sua busca? ")

    if "ajuda" in resposta or "perigo" in resposta:
        FN.write("Driade", "Seus motivos parecem sinceros. Sigam para o sul até o Vale Esmeralda. Lá encontrarão Lyra.")
    elif "equilíbrio" in resposta or "natureza" in resposta:
        FN.write("Driade", "Sigam pela trilha das estrelas à leste. Ela os aguardará na Clareira das Águas Tranquilas.")
    else:
        FN.write("Driade", "Seus corações parecem puros, mas o caminho até Lyra é perigoso. Siga a trilha da Lua Crescente ao oeste.")
    pl.parte = 5
    pl.save()
    encontrar_lyra(pl)

def encontrar_lyra(pl):
    """
    Função para simular o encontro com Lyra, a guardiã da floresta.
    """
    FN.write("", "Vocês seguem o caminho e encontram Lyra, a guardiã da floresta.")
    FN.write("Lyra", "Sou Lyra, um passarinho verde me contou que alguns jovens estavam atrás de mim, o que desejam?")
    
    ope = ["Encontrar o Rei.", "Somos apenas meros servos da Rainha Bruxa.", "Queremos um combate."]
    title = "Escolha uma opção:"
    menu = MN.menu(ope, 2, 2, title)
    menu.draw(0)
    menu.wait()
    escolha = menu.ans
    menu.close()

    if escolha == 0:
        FN.write("Lyra", "Lamento, mas não posso ajudá-los nesse assunto.")
        FN.write("", "Lyra desaparece diante de vocês, deixando-os sem ajuda.")
    elif escolha == 1:
        FN.write("Lyra", "Vejo que vocês têm boas intenções. Aqui está o mapa até a caverna dos Ladrões.")
        pl.xp += 10  # Ganha 10 XP
        FN.write("", "Vocês ganham o mapa e 10 pontos de experiência!")
    elif escolha == 2:
        FN.write("Lyra", "Se é um combate que desejam, assim seja.")
        pl.parte = 6
        iniciar_combate_lyra()
    pl.parte = 7
    pl.save()

def iniciar_combate_lyra(pl):
    FN.write("", "Você decide entrar em combate com Lyra.")
    FN.write("Lyra", "Preparem-se para enfrentar minha magia!")
    
    ope = ["Atacar Lyra", "Merlim interrompe", "Fugir"]
    title = "Escolha uma opção"
    menu = MN.menu(ope, 2, 2, title)
    menu.draw(0)
    menu.wait()
    escolha_combate = menu.ans
    menu.close()

    if escolha_combate == 0:
        pl.hp -= 20  # Perde 20 HP
        FN.write("", "Você ataca Lyra e sofre dano!")
        if pl.hp <= 0:
            FN.write("", "Seu HP está baixo, beba a poção de cura!")
    elif escolha_combate == 1:
        FN.write("Merlim", "Pare com isso, Lyra! Não precisamos lutar.")
        pl.xp += 10  # Ganha 10 XP
        FN.write("", "Merlim interrompe o combate e vocês ganham 10 pontos de experiência!")
    elif escolha_combate == 2:
        FN.write("", "Você decide fugir do combate.")
        FN.write("", "Lyra deixa vocês partirem, mas com uma advertência.")
    pl.parte = 6.1
    pl.save()