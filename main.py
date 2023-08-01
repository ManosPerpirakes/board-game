from pygame import *
from random import randint
init()

class Button():
    def __init__(self, text, window, x = 100, y = 100, width = 500, height = 50, colour = (255, 255, 255)):
        self.rect = rect.Rect(x, y, width, height)
        self.colour = colour
        self.window = window
        self.text = font.SysFont('Arial', height).render(text, True, (0, 0, 0))
    def show(self):
        draw.rect(self.window, self.colour, self.rect)
        self.window.blit(self.text, (self.rect.x, self.rect.y))
    def click(self, function):
        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            x, y = i.pos
        try:
            if self.rect.collidepoint(x, y) and b1wasclicked:
                function()
                function()
            if self.rect.collidepoint(x, y) and b1wasclicked == False:
                function()
        except:
            pass

def b1clicked():
    global players
    global b1wasclicked
    players = 2
    b1wasclicked = True

def b2clicked():
    global players
    players = 2

def b3clicked():
    global players
    players = 3

def b4clicked():
    global players
    players = 4

def rolldicef():
    global turn
    global playerwhowon
    global close
    global dicenumber
    global dicenumber2
    if b1wasclicked:
        if turn == 0:
            dicenumber = randint(1, 6)
        elif turn == 1:
            dicenumber2 = randint(1, 6)
    else:
        dicenumber = randint(1, 6)
    for i in range(dicenumber):
        if playerlist[turn].x < 540:
            playerlist[turn]. y -= 50
            playerlist[turn].x += 450
        else:
            playerlist[turn].x -= 50
        if playerlist[turn].y < 100:
            playerwhowon = turn + 1
            close = True
        for j in greenrectangles:
            if playerlist[turn].colliderect(j) and i == (dicenumber - 1):
                for i in range(5):
                    if playerlist[turn].x < 540:
                        playerlist[turn]. y -= 50
                        playerlist[turn].x += 450
                    else:
                        playerlist[turn].x -= 50
                    if playerlist[turn].y < 100:
                        playerwhowon = turn + 1
                        close = True
        for r in redrectangles:
            if playerlist[turn].colliderect(r) and i == (dicenumber - 1):
                for i in range(5):
                    if playerlist[turn].x > 950:
                        playerlist[turn]. y += 50
                        playerlist[turn].x -= 450
                    else:
                        playerlist[turn].x += 50
    turn += 1
    if turn > (players - 1):
        turn = 0
    draw.rect(w, (0, 255, 0), rect.Rect(1050, 300, 50, 50))

closew = False
while closew != True:
    b1wasclicked = False
    w = display.set_mode((1500, 750))
    display.set_caption('Board game')
    clock = time.Clock()
    players = None
    b1 = Button('1 player', w)
    b2 = Button('2 players', w, 100, 150)
    b3 = Button('3 players', w, 100, 200)
    b4 = Button('4 players', w, 100, 250)
    buttons = [b1, b2, b3, b4]
    functions = [b1clicked, b2clicked, b3clicked, b4clicked]
    close = False
    while close != True:
        w.fill((255, 255, 255))
        for i in event.get():
            if i.type == QUIT:
                closew = True
            if i.type == MOUSEBUTTONDOWN and i.button == 1:
                x, y = i.pos
        try:
            for i in range(4):
                if buttons[i].rect.collidepoint(x, y):
                    close = True
                    functions[i]()
        except:
            pass
        for i in buttons:
            i.show()
        display.update()
        clock.tick(60)
    rectangles = []
    x = 500
    y = 100
    for i in range(10):
        for j in range(10):
            rectangles.append(rect.Rect(x, y, 40, 40))
            x += 50
        y += 50
        x = 500
    x = 950
    y -= 50
    playerlist = []
    try:
        for i in range(players):
            if i == 1:
                x += 20
            if i == 2:
                x -= 20
                y += 20
            if i == 3:
                x += 20
            playerlist.append(rect.Rect(x, y, 20, 20))
    except:
        pass
    close = False
    greenrectangles = [rect.Rect(600, 300, 40, 40), rect.Rect(800, 200, 40, 40), rect.Rect(500, 500, 40, 40), rect.Rect(700, 400, 40, 40), rect.Rect(700, 100, 40, 40)]
    redrectangles = [rect.Rect(700, 300, 40, 40),  rect.Rect(650, 200, 40, 40), rect.Rect(600, 500, 40, 40), rect.Rect(600, 400, 40, 40), rect.Rect(650, 100, 40, 40)]
    dicenumber = None
    turn = 0
    while close != True:
        w.fill((255, 255, 255))
        w.blit(font.SysFont('Arial', 50).render('press space to roll the dice', True, (255, 0, 0)), (500, 50))
        for i in event.get():
            if i.type == QUIT:
                closew = True
            if i.type == KEYDOWN:
                if i.key == K_SPACE:
                    if b1wasclicked: 
                        rolldicef()
                        rolldicef()
                    else:
                        rolldicef() 
        if closew:
            close = True
        for i in rectangles:
            draw.rect(w, (0, 0, 255), i)
        for i in greenrectangles:
            draw.rect(w, (0, 255, 0), i)
        for i in redrectangles:
            draw.rect(w, (255, 0, 0), i)
        counter = len(rectangles)
        for i in rectangles:
            w.blit(font.SysFont('Arial', 20).render(str(counter), True, (255, 255, 255)), (i.x, i.y))
            counter -= 1
        try:
            draw.rect(w, (255, 255, 0), playerlist[0])
            draw.rect(w, (255, 0, 255), playerlist[1])
            draw.rect(w, (0, 0, 0), playerlist[2])
            draw.rect(w, (0, 255, 255), playerlist[3])
        except:
            pass
        if b1wasclicked:
            if dicenumber != None and dicenumber2 != None:
                w.blit(font.SysFont('Arial', 50).render("dice1: " + str(dicenumber), True, (255, 0, 0)), (1100, 300))
                w.blit(font.SysFont('Arial', 50).render("dice2: " + str(dicenumber2), True, (255, 0, 0)), (1100, 350))
        else:
            if dicenumber != None:
                w.blit(font.SysFont('Arial', 50).render("dice: " + str(dicenumber), True, (255, 0, 0)), (1100, 300))
        display.update()
        clock.tick(60)
    close = False
    while close != True:
        w.fill((255, 255, 255))
        for i in event.get():
            if i.type == QUIT:
                closew = True
            if i.type == KEYDOWN:
                if i.key == K_1:
                    close = True
        if closew:
            close = True  
        try:
            if b1wasclicked and playerwhowon == 1:
                w.blit(font.SysFont('Arial', 70).render('You win (1-try again)', True, (0, 255, 0)), (100, 100)) 
            if b1wasclicked and playerwhowon == 2:
                w.blit(font.SysFont('Arial', 70).render('You lose (1-try again)', True, (0, 255, 0)), (100, 100)) 
            if b1wasclicked == False:
                w.blit(font.SysFont('Arial', 70).render('player ' + str(playerwhowon) + ' won! (1-try again)', True, (0, 255, 0)), (100, 100))
        except:
            pass
        display.update()
        clock.tick(60)