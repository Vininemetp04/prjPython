import random

# Função para iniciar o Capítulo 5
def capitulo_5():
    with open("aventura.txt", "a") as FN:
        FN.write("Capítulo 5: A Batalha Final\n\n")
        FN.write("No covil do Feiticeiro Sombrio, uma batalha épica aguarda. Vocês entram na sala principal e veem o Feiticeiro Sombrio de pé, com um olhar ameaçador e uma aura de poder maligno ao seu redor.\n")
        FN.write("Feiticeiro Sombrio: 'Ah, vejo que meus pequenos intrusos finalmente chegaram. Vocês realmente acham que podem me derrotar e libertar o Rei Aric IV?'\n")
    
    resposta_merlim = input("Merlim: 'MARLEC? Você é o Feiticeiro Sombrio?' (Responda 'sim' ou 'não'): ")
    
    if resposta_merlim.lower() == 'sim':
        with open("aventura.txt", "a") as FN:
            FN.write("Feiticeiro Sombrio / Marlec: Todos esses anos, meu irmão tomou o que era meu, então eu decidi que era minha hora de tomar o que era dele. E por isso, eu irei acabar com o reino dele e seu reinado.\n")
    else:
        with open("aventura.txt", "a") as FN:
            FN.write("Feiticeiro Sombrio / Marlec: Então venham, quero ver do que são capazes.\n")
    
    # Iniciar a batalha final
    batalha_final()

    with open("saida.txt", "w") as FN:
    FN.write("Batalha Final: Feiticeiro Sombrio\n")
    FN.write(f"Feiticeiro Sombrio: {feiticeiro_hp} HP\n")
    FN.write(f"Seu HP: {seu_hp}\n")

    while feiticeiro_hp > 0 and seu_hp > 0:
        FN.write("\nEscolha sua ação:\n")
        FN.write("1: Utilizar a Espada Fantasma\n")
        FN.write("2: Utilizar a Lança Celestial\n")
        FN.write("3: Utilizar o Elixir da Força\n")
        FN.write("4: Utilizar o Amuleto da Sorte\n")

        opcao = input("Opção: ")

        if opcao == '1':
            dano = 50
            contra_ataque = random.randint(10, 20)
        elif opcao == '2':
            dano = 70
            contra_ataque = random.randint(0, 30)
        elif opcao == '3':
            dano = 250
            contra_ataque = random.randint(0, 40)
            seu_hp = 300  # Recupera todo o HP após utilizar o Elixir da Força
        elif opcao == '4':
            FN.write("Você usa o Amuleto da Sorte, aumentando suas chances de desviar dos ataques do Feiticeiro pelos próximos três turnos.\n")
            continue
        else:
            FN.write("Opção inválida. Escolha novamente.\n")
            continue

        feiticeiro_hp -= dano
        seu_hp -= max(0, contra_ataque)

        FN.write(f"Você causou {dano} de dano ao Feiticeiro Sombrio.\n")
        FN.write(f"O Feiticeiro Sombrio contra-atacou, causando {max(0, contra_ataque)} de dano.\n")

        FN.write(f"\nFeiticeiro Sombrio: {feiticeiro_hp} HP\n")
        FN.write(f"Seu HP: {seu_hp}\n")
