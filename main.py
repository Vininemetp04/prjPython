import os
import chracther as CH

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    pl = CH.Characther()
    pl.charactherCreator()
    pl.showCharacther()

if __name__ == "__main__":
    main()