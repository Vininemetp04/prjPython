import os
import characther as CH

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    pl = CH.Characther()
    pl.charactherCreator()

if __name__ == "__main__":
    main()