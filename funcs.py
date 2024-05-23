import os, sys
import time

TERM = os.get_terminal_size() # [coll(w), lines(h)] 

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
  
def strToPrtXYDl(str):
    arr = str.split("\033")
    cor = []
    arrCor = []
    for i in range(1, len(arr)):
        cor.append(f'\033{arr[i][0:6]}')
        arr[i] = arr[i][6:]
    for a in range(0, len(arr)):
        arrCor.append(arr[a])
        if a < len(cor):
            arrCor.append(cor[a])
    return arrCor

def prtXY(text, x=0, y=0):
    sys.stdout.write("\033[{};{}H".format(y, x))
    sys.stdout.write("\033[K")
    sys.stdout.write(text)
    sys.stdout.flush()

def prtXYDl(text, x=0, y=0):
    l = 0
    safeX = x
    safeY = y
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
                time.sleep(.03)     	
            x = x+lenPLV
        else:
            prtXY('║', TERM[0], TERM[1]-(4))
            y += 1
            l += 1
            x = safeX
            if l == 3:
                l = 0
                y = safeY
                input()

    prtXY('║', TERM[0], TERM[1]-(4))

def drawFrame(x, y, w, h):
    txtF = '╔' + '═'*(w-2) + '╗'
    time.sleep(.03)
    txtF1 = '╚' + '═'*(w-2) + '╝'
    time.sleep(.03)
    txtL = '║' + ' '*(w-2) + '║'
    prtXY(txtF, x+1, y+1)
    for i in range(0, h-2):
        time.sleep(.03)
        prtXY(txtL ,x+1, y+i+2)
    prtXY(txtF1, (x+1), (y+h))

#
# CAIXA DE DIALOGO
#

def wNome(q, cln=0):
    # Escreve nome
    q = "| "+q+' |'
    q = q + '═'*(TERM[0]-(len(q)+cln)-4) + '╗'
    prtXY(q, 4, TERM[1]-5)

def write(q, f, cln=0):
    wNome(q, cln)

    #escreve a fala
    fPalavras = f.split(' ')
    prtXYDl(fPalavras, 5, TERM[1]-4)
    # Sair e limpar quadro
    #KB.wait('enter')
    input()
    drawFrame(0, TERM[1]-6, TERM[0], 6)

def textColor(text, color):
    return f'{listColors[color]}{text}{listColors["white"]}'

def cls():
    os.system("cls" if os.name == "nt" else "clear")