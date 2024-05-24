import os, p1, funcs
import characther as CH
import cursor as CUR
import menu as MN
CUR.hide()

def readSave():
    save = open('save','r')
    dado = save.read().split('!@#@!')
    pl = CH.Characther()
    pl.charactherCreatorFormSave(dado)
    print(f'Bem-vindo de volta {pl.showName()}')
    if int(dado[7]) == 0:
        p1.start(pl)

def main():
    funcs.cls()
    CUR.show()
    if os.path.isfile('./save'):
        CUR.hide()
        mn = MN.menu(['Continuar save', 'Recomeçar'], 2, 2)
        mn.draw()
        MN.wait('enter')
        if mn.ans == 0:
            funcs.cls()
            readSave()
        else:
            funcs.cls()
            os.remove('./save')
            pl = CH.Characther()
            pl.charactherCreator()
            p1.start(pl)
    else:    
        pl = CH.Characther()
        pl.charactherCreator()
        CUR.hide()
        p1.start(pl)

if __name__ == "__main__":
    main()
    CUR.show()