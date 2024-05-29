import os, funcs as FN
import p1,p2
import characther as CH
import menu as MN

def readSave():
    save = open('save','r')
    dado = save.read().split(';')
    pl = CH.Characther()
    pl.charactherCreatorFormSave(dado)
    print(f'Bem-vindo de volta {pl.showName()}')
    match pl.parte:
        case '0':
            p1.start(pl)
        case '1':
            p2.decidir_acompanhamento_aria(pl)
        case '2':
            p2.encontro_com_rainha_bruxa(pl)
        case '3':
            p2.encontro_com_rainha_bruxa2(pl)
        case '4':
            p2.encontrar_driade(pl)
        case '5':
            p2.encontrar_lyra(pl)
        case '6':
            p2.iniciar_combate_lyra(pl)
        case '6.1':
            print('WIP')
        case '7':
            print('WIP')
            #p2.(pl)

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
    # FN.cls()
    input("Precione enter para sair")
    FN.cls()
    print("FAZ O L")
    print("LLLLL")
    print("LLLLL")
    print("LLLLL")
    print("LLLLL")
    print("LLLLL")
    print("LLLLL")
    print("LLLLL")
    print("LLLLLLLLLLLLLLL")
    print("LLLLLLLLLLLLLLL")
    print("LLLLLLLLLLLLLLL")
    #os.remove("./__pycache__")