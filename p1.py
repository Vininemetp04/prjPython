import time
import funcs as FN 
import menu as MN
import menu as MN

ATRASO = 1.2

def start(pl):
    time.sleep(ATRASO)  
    
    FN.write('Narrador', f"O mundo era feliz com reinado de Aric IV, você é um simples {pl.showType()}, apenas servindo ao seu reino, um dia triste, o rei misteriosamente e o mago Merlin, seu grande amigo, te chama para ir atrás do Rei")
    FN.write('Narrador', f"O mundo era feliz com reinado de Aric IV, você é um simples {pl.showType()}, apenas servindo ao seu reino, um dia triste, o rei misteriosamente e o mago Merlin, seu grande amigo, te chama para ir atrás do Rei")
    
    FN.write("Merlim: ", "Meu caro amigo, vamos atrás do rei, ele sumiu misteriosamente e agora o reino está sob o comando de Marlec, seu irmão.")
   
    FN.write(f"{pl.showName()}: ",f"Merlim, eu sou um mero {pl.showType()}, como posso ajudar um rei?", cln=-14)

    FN.textColor('Inicio', 'title')
    time.sleep(ATRASO)
    # Chegada ao Reino de Eldoria
    FN.write("Narrador: ","Ao chegar às portas do Reino de Eldoria, você encontra Aria, uma arqueira élfica.")
    FN.write("Narrador: ","Ao chegar às portas do Reino de Eldoria, você encontra Aria, uma arqueira élfica.")

    # Diálogo com Aria
    FN.write("Aria: ","Saudações, viajantes. Sou Aria, a guardiã destas florestas. O que os traz a Eldoria?")
    FN.write("Merlim:","Estamos em busca do Rei Aric IV, que desapareceu misteriosamente. Precisamos de sua ajuda, Aria.")
    FN.write("Aria: ","Saudações, viajantes. Sou Aria, a guardiã destas florestas. O que os traz a Eldoria?")
    FN.write("Merlim:","Estamos em busca do Rei Aric IV, que desapareceu misteriosamente. Precisamos de sua ajuda, Aria.")

    # Opções para o jogador
    FN.write("Aria: ","Eu posso ajudar, mas primeiro preciso saber suas intenções. Escolha com cuidado.")

    opeFmenu = ['Estamos aqui para salvar o reino. Por favor, nos ajude.', 'Nós precisamos de suas habilidades, mas não temos tempo a perder.', 'Se você se recusar a ajudar, encontraremos outro caminho.']
    menu1 = MN.menu(opeFmenu, 2, 2, "Faça sua escolha: ")
    menu1.draw(0)
    menu1.wait()
    ans = menu1.ans
    menu1.close()
    match ans:
        case 0:
            FN.write("Aria", "Vejo que suas intenções são nobres. Eu ajudarei vocês. Aqui, aceite esta poção de cura.")
            FN.write("", "Você recebeu uma Poção de Cura!")
            # Adiciona item de cura ao inventário do jogador
        case 1:
            FN.write("Aria", "Vejo que estão com pressa. Vamos direto ao ponto. Cuidado, a jornada será perigosa.")
            # Sem consequências diretas, mas aviso de perigo
        case 2:
            FN.write("Narrador: ", "Você e Merlim foram atacados por bandidos nas proximidades!")
            FN.write("Aria", "Se essa é sua atitude, terão que enfrentar as consequências. Defendam-se!")
            # Iniciar batalha ou causar dano ao jogador
    FN.write("Aria: ","Eu posso ajudar, mas primeiro preciso saber suas intenções. Escolha com cuidado.")

    opeFmenu = ['Estamos aqui para salvar o reino. Por favor, nos ajude.', 'Nós precisamos de suas habilidades, mas não temos tempo a perder.', 'Se você se recusar a ajudar, encontraremos outro caminho.']
    menu1 = MN.menu(opeFmenu, 2, 2, "Faça sua escolha: ")
    menu1.draw(0)
    menu1.wait()
    ans = menu1.ans
    menu1.close()
    match ans:
        case 0:
            FN.write("Aria", "Vejo que suas intenções são nobres. Eu ajudarei vocês. Aqui, aceite esta poção de cura.")
            FN.write("", "Você recebeu uma Poção de Cura!")
            # Adiciona item de cura ao inventário do jogador
        case 1:
            FN.write("Aria", "Vejo que estão com pressa. Vamos direto ao ponto. Cuidado, a jornada será perigosa.")
            # Sem consequências diretas, mas aviso de perigo
        case 2:
            FN.write("Narrador: ", "Você e Merlim foram atacados por bandidos nas proximidades!")
            FN.write("Aria", "Se essa é sua atitude, terão que enfrentar as consequências. Defendam-se!")
            # Iniciar batalha ou causar dano ao jogador