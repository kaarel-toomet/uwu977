## Building block definitions and related code
import pygame as pg

SKY = 0
BLOCK = 1
RBLOCK = 2
GROUND = 3

blocks = {}
# initialize empty dictionary, to be filled with loadBlocks
# as soon as we know the size
bn = {}

def loadBlocks(size):
    ## load blocks and scale to size
    global blocks, bn
    block = pg.transform.scale(pg.image.load("asdfblock.png"),
                               (size, size))
    rblock = pg.transform.scale(pg.image.load("redblock.png"),
                                (size, size))
    sky = pg.transform.scale(pg.image.load("sky.png"),
                             (size, size))
    ground = pg.transform.scale(pg.image.load("ground.png"),
                                (size, size))
    ## set up the blocks dictionary
    blocks = { SKY:sky, BLOCK:block, RBLOCK:rblock, GROUND:ground }
    bn={0:"air",1:"asdf",2:"redstuff",3:"ground"}

