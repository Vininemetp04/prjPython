import funcs as FN 
import random

def capitulo4():
    # Inicializar variáveis
    aria_acompanhando = True  # Exemplo, alterar conforme a situação

    def comer_pao(pl):
        pl.hp = 100
        FN.write("", "Você comeu o pão e recuperou todo o seu HP!")

    def beber_agua(pl):
        pl.hp += 50
        if pl.hp > 100:
            pl.hp = 100
        FN.write("", "Você bebeu a água e recuperou 50 HP!")

    def escolha_item(pl):
        FN.write("", "Escolha um tesouro:")
        FN.write("", "1. Lança Celestial")
        FN.write("", "2. Cajado da Ressurreição")
        FN.write("", "3. Amuleto da Sorte")
        escolha = input("Escolha uma opção (1, 2 ou 3): ")
        if escolha == '1':
            FN.write("", "Você escolheu a Lança Celestial!")
        elif escolha == '2':
            FN.write("", "Você escolheu o Cajado da Ressurreição!")
        elif escolha == '3':
            FN.write("", "Você escolheu o Amuleto da Sorte!")
        else:
            FN.write("", "Escolha inválida, você não recebeu um tesouro.")

    # Texto do Capítulo 4
    FN.write("", "Capítulo 4: A Jornada Continua\n")

    FN.write("", "Após saírem da toca dos ladrões, vocês, Merlim e Aria (se ela estiver acompanhando), iniciam sua jornada.")
    FN.write("", "O primeiro local onde devem parar é no Castelo de Baltazar, um antigo Clérigo chamado Gandar, o Bom.\n")

    FN.write("Gandar", "Bem-vindos, o que os traz à nossa humilde casa?\n")
    FN.write("Merlim", "Olá, Gandar. Viemos atrás do Sacerdote Baltazar. Estamos em busca de ajuda para recuperarmos o Rei.\n")
    FN.write("Gandar", "Creio que enfrentaram diversas batalhas até chegarem à nossa casa. Tomem e descansem, enquanto verifico se Baltazar pode atendê-los.\n")

    FN.write("", "Opção 1 > Comer pão")
    FN.write("", "Recupera XP total")
    FN.write("", "Opção 2 > Beber água")
    FN.write("", "Recupera 50 XP\n")

    escolha = input("Escolha uma opção (1 ou 2): ")
    if escolha == '1':
        comer_pao()
    elif escolha == '2':
        beber_agua()
    else:
        FN.write("", "Escolha inválida, não recuperou HP.\n")

    FN.write("", "\nGandar volta após alguns minutos em desespero.\n")

    FN.write("Gandar", "Sequestraram nosso mestre! Grita por toda a residência.\n")
    FN.write("Gandar", "O feiticeiro o sequestrou. Vocês podem me ajudar a recuperar meu mestre? Posso segui-los durante a viagem.\n")
    FN.write("Merlim", "Não vejo problema nisso.\n")

    FN.write("", "Gandar se une a nós e você pode escolher um tesouro:\n")

    escolha_item()
