
import funcs as FN 

ATRASO = 1.2

# Chegada ao Reino de Eldoria
FN.write("Ao chegar às portas do Reino de Eldoria, você encontra Aria, uma arqueira élfica.\n")

# Diálogo com Aria
FN.write("Aria: 'Saudações, viajantes. Sou Aria, a guardiã destas florestas. O que os traz a Eldoria?'\n")
FN.write("Merlim: 'Estamos em busca do Rei Aric IV, que desapareceu misteriosamente. Precisamos de sua ajuda, Aria.'\n")

# Opções para o jogador
FN.write("Aria: 'Eu posso ajudar, mas primeiro preciso saber suas intenções. Escolha com cuidado.'\n")
FN.write("1. 'Estamos aqui para salvar o reino. Por favor, nos ajude.'\n")
FN.write("2. 'Nós precisamos de suas habilidades, mas não temos tempo a perder.'\n")
FN.write("3. 'Se você se recusar a ajudar, encontraremos outro caminho.'\n")

# Escolha do jogador
escolha = input("Escolha uma opção (1, 2 ou 3): ")

if escolha == '1':
    FN.write("\nAria: 'Vejo que suas intenções são nobres. Eu ajudarei vocês. Aqui, aceite esta poção de cura.'")
    FN.write("Você recebeu uma Poção de Cura!")
    # Adiciona item de cura ao inventário do jogador
elif escolha == '2':
    FN.write("\nAria: 'Vejo que estão com pressa. Vamos direto ao ponto. Cuidado, a jornada será perigosa.'")
    # Sem consequências diretas, mas aviso de perigo
elif escolha == '3':
    FN.write("\nAria: 'Se essa é sua atitude, terão que enfrentar as consequências. Defendam-se!'")
    FN.write("Você e Merlim foram atacados por bandidos nas proximidades!")
    # Iniciar batalha ou causar dano ao jogador
else:
    FN.write("\nEscolha inválida. Tente novamente.")
    
FN.cls()
