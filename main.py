
import os, p1, funcs as FN
import characther as CH
import menu as MN

def readSave():
    save = open('save','r')
    dado = save.read().split('!@#@!')
    pl = CH.Characther()
    pl.charactherCreatorFormSave(dado)
    print(f'Bem-vindo de volta {pl.showName()}')
    if int(dado[7]) == 0:
        p1.start(pl)

def main():
    FN.cls()
    if os.path.isfile('./save'):
        mn = MN.menu(['Continuar save', 'Recomeçar'], 2, 2, "Bem Vindo de volta")
        mn.draw(0)
        mn.wait()
        ans = mn.ans
        mn.close()
        if ans == 0:
            FN.cls()
            readSave()
        else:
            FN.cls()
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
    input("Precione enter para sair")
    os.remove("./__pycache__")
    FN.cls()