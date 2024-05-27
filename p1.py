import time
import funcs as FN 

ATRASO = 1.2

def start(pl):
    time.sleep(ATRASO)  
    FN.drawFrame(0, FN.TERM[1]-6, FN.TERM[0], 6)
    
    FN.write('Deus', f"O mundo era feliz com reinado de Aric IV, você é um simples {pl.showType()}, apenas servindo ao seu reino, um dia triste, o rei misteriosamente e o mago Merlin, seu grande amigo, te  chama para ir atrás do Rei")
    
    FN.write("Merlim: ", "Meu caro amigo, vamos atrás do rei, ele sumiu misteriosamente e agora o reino está sob o comando de Marlec, seu irmão.")
   
    FN.write(f"{pl.showName()}: ",f"Merlim, eu sou um mero {pl.showType()}, como posso ajudar um rei?", cln=-14)

    FN.textColor('Inicio', 'title')
    time.sleep(ATRASO)
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

    escolha = input("Escolha uma opção (1, 2 ou 3): ")

if FN.escolha == '1':
    FN.write("Aria", "\n'Vejo que suas intenções são nobres. Eu ajudarei vocês. Aqui, aceite esta poção de cura.'")
    FN.write("", "Você recebeu uma Poção de Cura!")
    # Adiciona item de cura ao inventário do jogador
elif FN.escolha == '2':
    FN.write("Aria", "\n'Vejo que estão com pressa. Vamos direto ao ponto. Cuidado, a jornada será perigosa.'")
    # Sem consequências diretas, mas aviso de perigo
elif FN.escolha == '3':
    FN.write("Aria", "\n'Se essa é sua atitude, terão que enfrentar as consequências. Defendam-se!'")
    FN.write("", "Você e Merlim foram atacados por bandidos nas proximidades!")
    # Iniciar batalha ou causar dano ao jogador
else:
    FN.write("", "\nEscolha inválida. Tente novamente.")
    FN.cls()