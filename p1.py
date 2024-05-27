import time
import funcs as FN 

ATRASO = 1.2

def start(pl):
    time.sleep(ATRASO)  
    FN.drawFrame(0, FN.TERM[1]-6, FN.TERM[0], 6)
    
    FN.write('Deus', f"O mundo era feliz com reinado de Aric IV, você é um simples {pl.showType()}, apenas servindo ao seu reino, um dia triste, o rei misteriosamente e o mago Merlin, seu grande amigo, te chama para ir atrás do Rei")
    
    FN.write("Merlim: ", "Meu caro amigo, vamos atrás do rei, ele sumiu misteriosamente e agora o reino está sob o comando de Marlec, seu irmão.")
   
    FN.write(f"{pl.showName()}: ",f"Merlim, eu sou um mero {pl.showType()}, como posso ajudar um rei?", cln=-14)
    
    FN.cls()

    print(FN.textColor('Inicio', 'title'))
    time.sleep(ATRASO)
    FN.cls()