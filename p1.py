import time
import main
from sys import stdout

ATRASO = 1.2

def digita(txt, txt1):
    print(txt, end='')
    for i in txt1:
        print(i, end="")
        stdout.flush()
        time.sleep(.02)
    input()

def start(pl):
    time.sleep(ATRASO)
    digita('', f"O mundo era feliz com reinado de Aric IV, você é um simples {pl.showType()}, apenas servindo ao seu reino, um dia triste, o rei misteriosamente e o mago Merlin, seu grande amigo, te  chama para ir atrás do Rei")
    
    digita("Merlim: ", "Meu caro amigo, vamos atrás do rei, ele sumiu misteriosamente e agora o reino está sob o comando de Marlec, seu irmão.")
   
    digita(f"{pl.showName()}: ",f"Merlim, eu sou um mero {pl.showType()}, como posso ajudar um rei?")
    
    main.cls()

    print("Inicio")
    time.sleep(ATRASO)
    main.cls()