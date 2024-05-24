import keyboard as KB
import funcs as FN

wait = KB.wait

class menu:
    def __init__(self, text, x, y):
        self.x = x
        self.y = y
        self.text = text
        tempW = 0
        for p in text:
            lP = len(self.__rmColorCode(p))
            if lP >tempW: tempW = lP 
        self.w = tempW
        self.h = len(text) + 2
        self.select = 0
        KB.add_hotkey("up arrow", self.__up)
        KB.add_hotkey("down arrow", self.__down)
        KB.add_hotkey('space', self.__setAns)

    def __rmColorCode(self, p):
        if len(p.split('\033')) > 1:
            return (p[7:len(p)-7])
        return p

    def __setAns(self):
        self.ans = self.select
        FN.cls()
    
    def __upDate(self):
        sl = self.select
        self.draw()
        d = self.w - len(self.__rmColorCode(self.text[sl])) + 1
        FN.prtXY(" ║ \033[1;30;47m"+self.__rmColorCode(self.text[sl])+"\033[0m"+" "*d+"║ ", self.x, self.y+sl+2)

    def __up(self):
        if self.select == 0: return
        self.select -= 1
        self.__upDate()

    def __down(self):
        if self.select == len(self.text)-1: return
        self.select += 1
        self.__upDate()

    def draw(self):
        FN.drawFrame(self.x, self.y, self.w+4, len(self.text)+2, dl=0)
        for p in range(0, len(self.text)):
            d = self.w - len(self.__rmColorCode(self.text[p])) + 1
            FN.prtXY(" ║ "+self.text[p]+' '*d+"║ ", self.x, self.y+p+2)