import funcs as FN 
import random

def caverna_dos_bandidos(pl):
    FN.write("", "A Rainha das Bruxas pede que você recupere um artefato roubado por bandidos que se escondem em uma caverna próxima.")
    FN.write("", "Esta missão secundária é crucial para obter mais informações sobre o paradeiro do Rei Aric IV.")

    # Verificar como o jogador interagiu com Lyra
    if pl.hp <= 0:
        FN.write("", "Como você atacou Lyra e sofreu danos, você decide iniciar a missão bebendo a poção de cura.")
        pl.hp = 100  # Recuperar HP
        FN.write("", "Você bebe a poção de cura e se prepara para a missão.")
    elif pl.xp >= 10:
        FN.write("", "Como Merlim interrompeu o combate e você ganhou experiência, Lyra lhe dá o mapa para a caverna dos bandidos.")
        FN.write("", "Você agradece a Lyra e parte para a caverna, com o mapa em mãos.")
    else:
        FN.write("", "Como você correu do combate com Lyra, você se perde na floresta.")
        FN.write("", "Felizmente, Merlim o encontra e, após explicar a situação, Lyra compreende e lhe dá o mapa para a caverna.")
        FN.write("", "Ela te adverte que na próxima vez irá transformá-lo em sapo.")

# Iniciar o Capítulo 3
caverna_dos_bandidos()

def caverna_dos_bandidos():
    FN.write("", "A Rainha das Bruxas pede que você recupere um artefato roubado por bandidos que se escondem em uma caverna próxima.")
    FN.write("", "Esta missão secundária é crucial para obter mais informações sobre o paradeiro do Rei Aric IV.")

    # Verificar como o jogador interagiu com Lyra
    if pl.hp <= 0:
        FN.write("", "Como você atacou Lyra e sofreu danos, você decide iniciar a missão bebendo a poção de cura.")
        pl.hp = 100  # Recuperar HP
        FN.write("", "Você bebe a poção de cura e se prepara para a missão.")
    elif pl.xp >= 10:
        FN.write("", "Como Merlim interrompeu o combate e você ganhou experiência, Lyra lhe dá o mapa para a caverna dos bandidos.")
        FN.write("", "Você agradece a Lyra e parte para a caverna, com o mapa em mãos.")
    else:
        FN.write("", "Como você correu do combate com Lyra, você se perde na floresta.")
        FN.write("", "Felizmente, Merlim o encontra e, após explicar a situação, Lyra compreende e lhe dá o mapa para a caverna.")
        FN.write("", "Ela te adverte que na próxima vez irá transformá-lo em sapo.")

# Iniciar o Capítulo 3
caverna_dos_bandidos()

def caverna_ladroes():
    FN.write("", "Ao entrar na caverna dos ladrões, você nota que ela está completamente escura.")
    FN.write("", "Você tem duas opções:")
    FN.write("", "1. Seguir na escuridão.")
    FN.write("", "2. Iluminar o caminho.")

    escolha_caverna = input("Escolha uma opção (1 ou 2): ")

    if escolha_caverna == '1':
        FN.write("", "Você decide seguir na escuridão. Nada acontece.")
    elif escolha_caverna == '2':
        FN.write("", "Você decide iluminar o caminho, acendendo uma tocha.")
        pl.tocha = True  # O personagem agora tem uma tocha
        FN.write("", "Enquanto ilumina o caminho, você nota esqueletos humanos jogados no chão.")
        FN.write("", "Ao seguir adiante, você ouve sons estranhos e sente um vento gelado.")
        FN.write("", "Sua tocha apaga repentinamente.")
        FN.write("", "Um fantasma surge diante de vocês.")
        FN.write("Merlim", "Nos perdoem, jamais imaginaríamos que vocês haviam falecidos. O que houve?")
        FN.write("", "Fantasma: Nós fomos mortos pelo dragão do Feiticeiro Sombrio.")
        FN.write("", "Fantasma: Nós nos opusemos a sequestrar o Rei, somos ladrões, mas somos honestos.")
        FN.write("Merlim", "Estamos atrás do Rei, queremos ajudá-lo a sair dessa situação.")
        FN.write("", "Fantasma dá uma espada para o Player.")
        FN.write("", "Fantasma: Esta é a única coisa que nos restou. Se você for valente o suficiente para seguir, ao final encontrará o dragão vermelho, ele está com nossas almas presas no Cálice Sagrado, este irá ajudar em seu caminho.")

        # Salvar informação: Ganhou espada
        pl.xp += 10  # Ganha 10 XP

        # Continuação da história
        continuar_caminho()

def continuar_caminho(pl):
    FN.write("", "Vocês seguem pela mina escura e encontram três pequenos baús.")

    # Escolha dos baús
    FN.write("", "Você irá:")
    FN.write("", "1. Escolher o Baú Cinza.")
    FN.write("", "2. Abrir o Baú Lilás.")
    FN.write("", "3. Encarar os esqueletos que se levantam.")

    escolha_baus = input("Escolha uma opção (1, 2 ou 3): ")

    if escolha_baus == '1':
        FN.write("", "Você escolhe o Baú Cinza e ganha 150 HP e 100 XP.")
        pl.hp += 150  # Ganha 150 HP
        pl.xp += 100  # Ganha 100 XP
    elif escolha_baus == '2':
        FN.write("", "Você abre o Baú Lilás e é atingido por veneno fatal. Você desmaia.")
        pl.hp = 0  # Reduz HP a 0
        pl.xp -= 30  # Perde 30 XP
        FN.write("", "Horas depois, Merlim o acorda e você perde 30 XP.")
    elif escolha_baus == '3':
        FN.write("", "Você decide encarar os esqueletos e inicia uma batalha.")
        batalha_esqueletos()
    else:
        FN.write("", "Escolha inválida.")

def batalha_esqueletos(pl):
    esqueleto_hp = 100

    FN.write("", "Você inicia a batalha contra os esqueletos.")

    while esqueleto_hp > 0:
        FN.write("", "Escolha sua ação:")
        FN.write("", "1. Ataque 1 (30 HP)")
        FN.write("", "2. Ataque 2 (10 HP)")
        FN.write("", "3. Ataque 3")

        escolha_ataque = input("Escolha uma opção (1, 2 ou 3): ")

        if escolha_ataque == '1':
            esqueleto_hp -= 30
            pl.hp -= 10  # Perde 10 HP devido ao ataque do esqueleto
            FN.write("", "Você ataca o esqueleto e causa 30 de dano.")
            FN.write("", "O esqueleto contra-ataca e você perde 10 de HP.")
        elif escolha_ataque == '2':
            esqueleto_hp -= 10
            pl.hp -= 5  # Perde 5 HP devido ao ataque do esqueleto
            FN.write("", "Você ataca o esqueleto e causa 10 de dano.")
            FN.write("", "O esqueleto contra-ataca e você perde 5 de HP.")
        elif escolha_ataque == '3':
            FN.write("", "Você tenta um ataque, mas não surte efeito.")
            FN.write("", "O esqueleto contra-ataca e você perde 10 de HP.")
            pl.hp -= 10  # Perde 10 HP devido ao ataque do esqueleto
        else:
            FN.write("", "Escolha inválida.")

    FN.write("", "Você derrota os esqueletos.")

# Chamada da função principal
caverna_ladroes()

def enfrentar_dragao(pl):
    FN.write("Merlim", "O que vamos fazer?")
    FN.write("", "1. Correr e se esconder.")
    FN.write("", "2. Atacar o dragão junto com Merlim.")
    FN.write("", "3. Usar a espada dos fantasmas.")

    escolha_dragao = input("Escolha uma opção (1, 2 ou 3): ")

    if escolha_dragao == '1':
        FN.write("", "Vocês decidem correr e se esconder. Nada acontece, mas você perde o jogo.")
        # Fim do jogo
    elif escolha_dragao == '2':
        FN.write("Merlim", "Juntos, vocês atacam o dragão.")
        FN.write("", "O dragão cai no chão e desmaia por algum tempo.")

        # Verifica se o dragão desmaiou
        dragao_desmaiado = True  # Supondo que o dragão desmaiou

        if dragao_desmaiado:
            FN.write("", "O dragão desmaia. Você tem 10 segundos para sair. Clique no espaço.")
            # Aqui você pode adicionar a lógica para esperar o jogador clicar no espaço
            FN.write("", "Você pega o cálice.")
            # Salvar: Pegou o cálice
            ganhar_tesouros_random()
            FN.write("", "Vocês saem da toca do dragão.")
            FN.write("", "Vocês recebem a benção e o mapa até o Covil do Feiticeiro.")
        else:
            # Caso o dragão não desmaie
            FN.write("", "O dragão acorda e vocês retornam para as opções.")
            enfrentar_dragao()  # Retorna para as opções
    elif escolha_dragao == '3':
        FN.write("", "Você usa a espada dos fantasmas e derrota o dragão, dando-lhe uma facada no coração.")
        # Salvar: Derrotou o dragão
        ganhar_tesouros_random()
        FN.write("", "Vocês pegam o cálice.")
        FN.write("", "Vocês saem da toca do dragão.")
        FN.write("", "Vocês recebem a benção e o mapa até o Covil do Feiticeiro.")
    else:
        FN.write("", "Escolha inválida.")

# Função para ganhar tesouros randoms
def ganhar_tesouros_random(pl):
    tesouros = ["Espada Encantada", "Poção de Cura", "Amuleto da Sorte", "Escudo Mágico", "Anel de Poder"]
    tesouros_obtidos = random.sample(tesouros, 3)  # Escolhe 3 tesouros aleatórios
    FN.write("", "Ao pegar o cálice, vocês devolvem as almas ao seu lugar real.")
    FN.write("", "Como recompensa, vocês ganham os seguintes tesouros:")
    for tesouro in tesouros_obtidos:
        FN.write("", f"- {tesouro}")

# Chamada da função para enfrentar o dragão
enfrentar_dragao()

class FN:
    @staticmethod
    def write(speaker, text):
        if speaker:
            print(f"{speaker}: {text}")
        else:
            print(text)

def capitulo4():
    # Inicializar variáveis
    aria_acompanhando = True  # Exemplo, alterar conforme a situação
    player_hp = 100  # HP inicial do jogador
    player_xp = 0  # XP inicial do jogador
    inventory = []

    # Parte 1: No Castelo de Baltazar
    FN.write("Gandar", "Bem-vindos, o que os traz à nossa humilde casa?")
    FN.write("Merlim", "Olá, Gandar. Viemos atrás do Sacerdote Baltazar. Estamos em busca de ajuda para recuperarmos o Rei.")
    FN.write("Gandar", "Creio que enfrentaram diversas batalhas até chegarem à nossa casa. Tomem e descansem, enquanto verifico se Baltazar pode atendê-los.")
    
    # Opções de descanso
    FN.write("", "Opção 1 > Comer pão")
    FN.write("", "Opção 2 > Beber água")

    escolha_descanso = input("Escolha uma opção (1 ou 2): ")
    if escolha_descanso == "1":
        player_hp = 100
        FN.write("", "Você comeu o pão e recuperou todo o seu HP!")
    elif escolha_descanso == "2":
        player_hp = min(player_hp + 50, 100)
        FN.write("", "Você bebeu água e recuperou 50 HP!")
    
    FN.write("Gandar", "Sequestraram nosso mestre! O feiticeiro o sequestrou. Vocês podem me ajudar a recuperar meu mestre? Posso segui-los durante a viagem.")
    FN.write("Merlim", "Não vejo problema nisso.")
    FN.write("", "Gandar se une a nós e você pode escolher um tesouro.")
    
    # Opções de tesouro
    FN.write("", "Opção 1 > Lança celestial")
    FN.write("", "Opção 2 > Cajado da ressurreição")
    FN.write("", "Opção 3 > Amuleto da sorte")

    escolha_tesouro = input("Escolha uma opção (1, 2 ou 3): ")
    if escolha_tesouro == "1":
        inventory.append("Lança celestial")
    elif escolha_tesouro == "2":
        inventory.append("Cajado da ressurreição")
    elif escolha_tesouro == "3":
        inventory.append("Amuleto da sorte")

    FN.write("Gandar", "Aquele salafraio! Sabíamos que ele não era confiável. Vejamos, para seguirmos, devemos ir até o Rio das Lamentações, onde nos encontraremos com Sereias. Devemos ter cuidado para não nos deixarmos seduzir. Após, iremos à Cidade Élfica de Silvadria, encontrar Elena, uma Ladina. Ela terá maiores informações sobre o paradeiro do rei.")

    # Parte 2: No Rio das Lamentações
    FN.write("", "Vocês seguem o caminho até o Rio das Lamentações. Gandar possuía um bom coração e seria útil caso vocês estivessem à beira da morte. Ele nos leva até o caminho, ao entardecer verificamos o rio à nossa frente, logo o silêncio profundo da floresta e o som da água correndo pelo rio se tornam o único som a ser escutado.")

    FN.write("*Rio das Lamentações*", "")

    FN.write("", "Ao chegarmos no rio, verificamos que não havia nada e nem ninguém. Até o início de uma cantiga, esta que inicia com apenas um som suave de uma cantoria.")
    FN.write("Gandar", "Cuidado, não se iludam, sereias não são belas criaturas. São seres mortíferos.")
    FN.write("", "Você nota a ausência de Merlim. Logo o vê indo até o rio.")
    FN.write("Você", "Merlim!")
    FN.write("Gandar", "Vamos buscá-lo antes que seja tarde.")

    # Opções para resgatar Merlim
    FN.write("", "Opção 1 > Corre até Merlim")
    FN.write("", "Opção 2 > Você joga a Lança Celestial")
    FN.write("", "Opção 3 > Você corre")

    escolha_resgate = input("Escolha uma opção (1, 2 ou 3): ")
    if escolha_resgate == "1":
        FN.write("", "Merlim cai no lago, porém você nada e consegue salvá-lo.")
        FN.write("Merlim", "Foi por pouco, obrigada amigo.")
        FN.write("", "Merlim te dá um 'Elixir da força' em agradecimento por salvá-lo.")
        inventory.append("Elixir da força")
    elif escolha_resgate == "2" and "Lança celestial" in inventory:
        FN.write("", "Você consegue atingir a sereia e Merlim se recupera.")
        FN.write("Merlim", "Foi por pouco, obrigada amigo.")
        FN.write("", "Merlim te dá um 'Elixir da força' em agradecimento por salvá-lo.")
        inventory.append("Elixir da força")
    elif escolha_resgate == "3":
        FN.write("", "Você cai no lago e morre.")
        FN.write("", "End Game")
        return
    
    FN.write("Gandar", "Vamos continuar.")
    
    # Parte 3: Encruzilhada
    FN.write("", "Vocês seguem o caminho, até que encontram uma encruzilhada. Você pode:")
    FN.write("", "Opção 1 > Ir à direita")
    FN.write("", "Opção 2 > Ir à esquerda")

    escolha_caminho = input("Escolha uma opção (1 ou 2): ")
    if escolha_caminho == "1":
        FN.write("", "Encontra um belo caminho com flores e fadas.")
        player_xp += 100
        FN.write("", "Você ganha 100 XP!")
    elif escolha_caminho == "2":
        FN.write("", "Encontra um troll.")
        FN.write("", "Batalha")
        troll_hp = 100
        while troll_hp > 0:
            FN.write("", "Opção 1 > Atacar com Espada Fantasma")
            FN.write("", "Opção 2 > Atacar usando outra arma")
            escolha_ataque = input("Escolha uma opção (1 ou 2): ")
            if escolha_ataque == "1":
                troll_hp -= 70
                FN.write("", "Você ataca com a Espada Fantasma, causando 70 de dano.")
                if troll_hp > 0:
                    player_hp -= 10
                    FN.write("", "O troll contra-ataca, você perde 10 HP.")
            elif escolha_ataque == "2":
                troll_hp -= 40
                FN.write("", "Você ataca com outra arma, causando 40 de dano.")
                if troll_hp > 0:
                    player_hp -= 5
                    FN.write("", "O troll contra-ataca, você perde 5 HP.")
        FN.write("", "Você matou o troll!")
        FN.write("", "Ganha: Pote de ouro")
        inventory.append("Pote de ouro")
    
    # Parte 4: Chegada ao castelo do Feiticeiro Sombrio
    FN.write("", "Após vocês finalmente chegam ao castelo do Feiticeiro Sombrio.")



