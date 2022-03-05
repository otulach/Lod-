from random import choice
random10 = [i for i in range(10)]
delkal = 4
deset = [i for i in range(10)]
sx = 1
sy = 1
dx = 0
dy = 0
c = 0
g = 0
i = 0
j = 0



def pridejd(vystrel, dx, dy, c):
    if dx <= 9:
        dx += 2
    elif dx == 10:
        dx -= 9
        dy += 1
    elif dx == 11:
        dx -= 11
        dy += 1
    elif dy == 9:
        c = 1

def s(vystrel, dx, dy):
    if vystrel[dy][dx] == ".":
        p = 1

    return p == 1
    
def oznac(vystrel, dx ,dy):
    vystrel[dy][dx] = "x"

def oznacvse(vystrel, dx, dy):
    oznac(vystrel, dx + 1 ,dy)
    oznac(vystrel, dx -1 ,dy)
    oznac(vystrel, dx ,dy + 1)
    oznac(vystrel, dx ,dy - 1)
    oznac(vystrel, dx ,dy)

def sejmiho(vystrel, dx, dy, i ,j):
    if g == 1:
        i += 1
        if dx + i > 9 or vystrel[dy + j][dx + i] == "x":
            g += 1
            i = 0
    if g == 2:
        i += -1
        if dx + i < 0 or vystrel[dy + j][dx + i] == "x":
            g += 1
            i = 0
    if g == 3:
        j += 1
        if dy + j > 9 or vystrel[dy + j][dx + i] == "x":
            g += 1
            j = 0
    if g == 4:
        j += -1

def random(dx, dy, deset):
    dx = choice(deset)
    dy = choice(deset)


def strileni(vystrel, delkal, dx, dy, g, i, j):
    if c == 1:
        random(dx, dy, deset)

    if vystrel[dy][dx] == "x" and c == 1:
        strileni(vystrel, delkal, dx, dy, g, i, j)
        
    if vystrel[dy][dx] == "x" and g < 1:
        pridejd(vystrel, dx, dy, c)
        strileni(vystrel, delkal, dx, dy, g, i, j)

    sejmiho(vystrel, dx, dy, i ,j)
    
    print(dx + i, dy + j)
    x = input()

    if x == "miss" and g >= 1:
        oznac(vystrel, dx ,dy)
        g += 1
        exit()
    if x == "miss":
        oznac(vystrel, dx ,dy)
        pridejd(vystrel, dx, dy, c)
    if x == "hit":
        oznacvse(vystrel, dx, dy)
        g = 1
    if x == "hit, sunk":
        oznacvse(vystrel, dx, dy)
        g = 0
        i = 0
        j = 0
    if x == "hit, sunk, end":
        pass
    
vystrel = []

strileni(vystrel, delkal, dx, dy, g, i, j)
