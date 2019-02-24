#!/usr/bin/env python3
import argparse
import pygame as pg
import random as r
import numpy as np

## Command line arguments
parser = argparse.ArgumentParser(description='UWU977: Crazy Hat builds a world!')
parser.add_argument('-v', type=int, default=0,
                    help='verbosity level')
parser.add_argument('-x', '--width', type=int, default=30,
                    dest='width',
                    help='world width (tiles)')
parser.add_argument('-y', '--height', type=int, default=10,
                    dest='height',
                    help='world height (tiles)')
args = parser.parse_args()

## ---------- initialize ----------
pg.init()
pg.mixer.init()
f=64
pic = pg.transform.scale(pg.image.load("pic.png"),(f,f))
block = pg.transform.scale(pg.image.load("asdfblock.png"),(f,f))
pg.font
screen = pg.display.set_mode((0,0), pg.RESIZABLE)
screenw = screen.get_width()
screenh = screen.get_height()
pg.display.set_caption("movepic")
do = True
dist = 1
actuallyuselessvariable = 39
up = True
down = True
left = True
right = True
mup = False
mdown = False
mleft = False
mright = False
timer = pg.time.Clock()
lifes = 5
font = pg.font.SysFont("Times", 24)
dfont = pg.font.SysFont("Times", 32)
pfont = pg.font.SysFont("Times", 50)
pause = False
gameover = False
sx=screenw/2
sy=screenh/2
player = pg.sprite.Group()
## ---------- Build the world ----------
## variables
worldWidth = args.width
worldHeight = args.height
groundLevel = 0.5
# in fraction, from bottom.  0.3 means bottom 30%
## sanity check
worldHeight = min(max(worldHeight, 2), 400)
worldWidth = min(max(worldWidth, 2), 2000)
if groundLevel < 0:
    groundLevel = 0
if groundLevel > 1:
    groundLevel = 1.0
world = np.zeros((worldHeight, worldWidth), 'int8')
iGround = int((1 - groundLevel)*worldHeight)
world[iGround:] = 1
## where crzy hat has her home:
homeX = int(worldWidth/2)
homeY = max(iGround - 1, 0)
## ---------- world done ----------
def tc(x,y):
    return(x*f+sx,y*f+sy)
class Player(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pic
        self.rect = self.image.get_rect()
        self.x=x
        self.y=y
        self.rect.x = tc(x,y)[0]
        self.rect.y = tc(x,y)[1]
    def update(self, mup, mdown, mleft, mright):
        global sx,sy,f
        d=0
        r=0
        if mup:
            d=-1
        if mdown:
            d=-1
        if mdown:
            d=1
        if mleft:
            r=-1
        if mright:
            r=1
        self.x+=r
        self.y+=d
        if self.x<0 or self.y<0 or self.x >= worldWidth or self.y >= worldHeight: # or world[self.y,self.x]==1:
            self.x-=r
            self.y-=d
        world[self.y,self.x] = 0
            #self.x-=r
            #self.y-=d
        #print(self.x, self.y)
        sx = screenw/2-hullmyts.getxy()[0]*f
        sy = screenh/2-hullmyts.getxy()[1]*f
        self.rect.x = tc(self.x,self.y)[0]
        self.rect.y = tc(self.x,self.y)[1]
    def getxy(self):
        return(self.x,self.y)
def reset():
    lifes = 5
    player.empty()
    hullmyts = Player(homeX, homeY)
    player.add(hullmyts)
hullmyts = Player(homeX, homeY)
player.add(hullmyts)
def build(x,y):
    s=world.shape
    if x>=0 and y>=0 and x<s[1] and y<s[0]:
        world[x,y] = 1
while do:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            do = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                mup = True  #useless comment
            elif event.key == pg.K_DOWN:
                mdown = True
            elif event.key == pg.K_LEFT:
                mleft = True
            elif event.key == pg.K_RIGHT:
                mright = True
            elif event.key == pg.K_a:
                build(hullmyts.getxy()[1],hullmyts.getxy()[0]-1)
            elif event.key == pg.K_s:
                build(hullmyts.getxy()[1]+1,hullmyts.getxy()[0])
            elif event.key == pg.K_d:
                build(hullmyts.getxy()[1],hullmyts.getxy()[0]+1)
            elif event.key == pg.K_w:
                build(hullmyts.getxy()[1]-1,hullmyts.getxy()[0])
            elif event.key == pg.K_p:
                pause = True
            elif event.key == pg.K_r:
                reset()
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                mup = False
            elif event.key == pg.K_DOWN:
                mdown = False
            elif event.key == pg.K_LEFT:
                mleft = False
            elif event.key == pg.K_RIGHT:
                mright = False
    while pause:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pause = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    pause = False
        pd = "PAUSED"
        ptext = dfont.render(pd, True, (127,127,127))
        ptext_rect = ptext.get_rect()
        ptext_rect.centerx = screen.get_rect().centerx
        ptext_rect.y = 50
        screen.blit(ptext,ptext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
    if lifes == 0:
        uded = "GAME OVER"
        dtext = dfont.render(uded, True, (255,0,0))
        dtext_rect = dtext.get_rect()
        dtext_rect.centerx = screen.get_rect().centerx
        dtext_rect.y = 30
        screen.blit(dtext,dtext_rect)
        screen.blit(text,text_rect)
        pg.display.update()
        gameover = True
    while gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = False
                do = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    gameover = False
                    reset()
    screen.fill((255,255,255))
    score = ("Lifes: " + str(lifes))
    text = font.render(score, True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text,text_rect)
    for x in range(world.shape[0]):
        for y in range(world.shape[1]):
            if world[x,y] == 1:
                screen.blit(block,tc(y,x))
    player.update(mup,mdown, mleft, mright)
    player.draw(screen)
    pg.display.update()
    mup = False
    mdown = False
    mleft = False
    mright = False
    timer.tick(60)

pg.quit()
