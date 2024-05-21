import os
import characther as CH
import p1

listColors = {
    'white': '\033[0;0;0m',
    'red': '\033[0;31m',
    'green': '\033[0;32m',
    'yellow': '\033[0;33m',
    'blue': '\033[0;34m',
    'purple': '\033[0;35m',
    'cyan': '\033[0;36m',
    'gray': '\033[1;37;40m'
}

def textColor(text, color):
    return f'{listColors[color]}{text}{listColors["white"]}'

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def readSave():
    save = open('save','r')
    dado = save.read().split('!@#@!')
    pl = CH.Characther()
    pl.charactherCreatorFormSave(dado)
    print(f'{dado[7]} ||| size {len(dado)} ||| {type(dado[7])} == 0 ={type(0)}')
    print(f'Bem-vindo de volta {pl.showName()}')
    if int(dado[7]) == 0:
        print('pao')
        p1.start(pl)

def main():
    cls()
    if os.path.isfile('./save'):
        c = int(input('[ 0 ] Não\n[ 1 ] Sim\nDeseja continuar da onde seu save? '))
        if c != 0:
            readSave()
        else:
            os.remove('./save')
            pl = CH.Characther()
            pl.charactherCreator()
            p1.start(pl)
    else:    
        pl = CH.Characther()
        pl.charactherCreator()
        p1.start(pl)

if __name__ == "__main__":
    main()