import os, sys, time, keyboard as KB, cursor as CUR

TERM = os.get_terminal_size() # [coll(w), lines(h)] 
show = CUR.show
hide = CUR.hide

listColors = {
    'title': '\033[1;97m',
    'white': '\033[0;00m',
    'red': '\033[0;31m',
    'green': '\033[0;32m',
    'yellow': '\033[0;33m',
    'blue': '\033[0;34m',
    'purple': '\033[0;35m',
    'cyan': '\033[0;36m',
    'gray': '\033[1;37m'
}
  
def prtXY(text, x=0, y=0):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.write("\033[K")
    sys.stdout.write(text)
    sys.stdout.flush()

def wirteOnBox(text, x=0, y=0):
    l = 0
    safeX = x
    safeY = y
    dl = .04
    for plv in range(0, len(text)):
        palavra = text[plv] + ' '
        if len(palavra.split('\033')) != 1:
            lenPLV = len(palavra) -14
        else: lenPLV = len(palavra)

        if x + lenPLV < TERM[0]-10:
            for i in range(0, len(palavra)):
                if i == 0:
                    prtXY(palavra[i], x+i, y)
                else:
                    print(palavra[i], end='')
                    sys.stdout.flush()
                time.sleep(dl)     	
            x = x+lenPLV
            prtXY('║', TERM[0], TERM[1]-(4-l))
        else:
            y += 1
            l += 1
            x = safeX
            if l == 3:
                l = 0
                y = safeY
                nextDl()
                drawFrame(0, TERM[1]-6, TERM[0], 6, 1)

def drawFrame(x, y, w, h, prt1=0, dl=.02):
    txtF =  '╔' + '═'*(w-2) + '╗'
    txtL =  '║' + ' '*(w-2) + '║'
    txtF1 = '╚' + '═'*(w-2) + '╝'
    if prt1 == 0: 
        prtXY(txtF, x+1, y+1)
    for i in range(0, h-2):
        time.sleep(dl)
        prtXY(txtL ,x+1, y+i+2)
        time.sleep(dl)
    prtXY(txtF1, (x+1), (y+h))

#
# CAIXA DE DIALOGO
#

def nextDl():
    prtXY('\/ ║', TERM[0]-3, TERM[1]-1)
    KB.wait('space')

def write(q, f, cln=0):
    drawFrame(0, TERM[1]-6, TERM[0], 6)
    q = "| "+q+' |'
    q = q + '═'*(TERM[0]-(len(q)+cln)-4) + '╗'
    
    prtXY(q, 4, TERM[1]-5)
    #escreve a fala
    fPalavras = f.split(' ')
    wirteOnBox(fPalavras, 5, TERM[1]-4)
    nextDl()
    drawFrame(0, TERM[1]-6, TERM[0], 6)

def textColor(text, color):
    return f'{listColors[color]}{text}{listColors["white"]}'

def cls():
    os.system("cls" if os.name == "nt" else "clear")

# def escolha():

    # opcoes_validas = ['1', '2', '3']  

    # while True:
        # escolha = input("Escolha uma opção (1, 2 ou 3): ")

        # if escolha in opcoes_validas:
            # return escolha  
        # else:
            # print("Escolha inválida. Por favor, escolha entre as opções 1, 2 ou 3.")

    # opcao_escolhida = escolha()
    # print("Você escolheu a opção:", opcao_escolhida)
