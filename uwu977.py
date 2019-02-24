#!/usr/bin/env python3
import pygame as pg
import random as r
import numpy as np
pg.init()
pg.mixer.init()
pic = pg.transform.scale(pg.image.load("pic.png"),(64,64))
block = pg.transform.scale(pg.image.load("asdfblock.png"),(64,64))
pg.font
screen = pg.display.set_mode((0,0), pg.RESIZABLE)
screenw = screen.get_width()
screenh = screen.get_height()
pg.display.set_caption("movepic")
do = True
dist = 1
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
player = pg.sprite.GroupSingle()
world = np.array([[0,0,0,0,0,0,0,0],
                  [1,0,1,1,0,0,1,1],
                  [1,1,0,0,0,1,0,0],
                  [0,0,0,1,0,0,0,1]])
def tc(x,y):
    return(x*64,y*64)
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
        d=0
        r=0
        if mup:
            #if self.y > 0:
            d=-1#    self.y -= 1
        if mdown:
            #if self.y < 
            #
            d=-1
        if mdown:
            d=1
        if mleft:
            r=-1
        if mright:
            r=1
        self.x+=r
        self.y+=d
        try:
            if self.x<0 or self.y<0 or world[self.y,self.x]==1:
                self.x-=r
                self.y-=d
        except:
            self.x-=r
            self.y-=d
        #print(self.x, self.y)
        self.rect.x = tc(self.x,self.y)[0]
        self.rect.y = tc(self.x,self.y)[1]
def reset():
    lifes = 5
    player.empty()
    hullmyts = Player(0,0)
    player.add(hullmyts)
hullmyts = Player(0,0)
player.add(hullmyts)
while do:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            do = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                mup = True
            elif event.key == pg.K_DOWN:
                mdown = True
            elif event.key == pg.K_LEFT:
                mleft = True
            elif event.key == pg.K_RIGHT:
                mright = True
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
