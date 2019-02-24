## Building block definitions and related code
import pygame as pg

SKY = 0
BLOCK = 1
RBLOCK = 2
GROUND = 3
BACKG = 4
PEBBL = 5
CORE = 6
STNBACK = 7
GOLD = 8
GWALL = 9
WINDOW = 10
GORE=11

breakable = set([BLOCK, RBLOCK, GROUND, PEBBL, CORE, GOLD, GORE])
breakto = {SKY:SKY,BLOCK:BACKG,RBLOCK:SKY,GROUND:SKY,BACKG:BACKG,PEBBL:STNBACK,CORE:STNBACK,STNBACK:STNBACK,GOLD:SKY,GWALL:GWALL,WINDOW:WINDOW,GORE:STNBACK}

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
    backg = pg.transform.scale(pg.image.load("asdfback.png"),
                                (size, size))
    pebbl = pg.transform.scale(pg.image.load("pebbl.png"),
                                (size, size))
    core = pg.transform.scale(pg.image.load("coalpebbl.png"),
                                (size, size))
    stnback = pg.transform.scale(pg.image.load("pebblbackg.png"),
                                (size, size))
    gold = pg.transform.scale(pg.image.load("goldblock.png"),
                                (size, size))
    gwall = pg.transform.scale(pg.image.load("goldwall.png"),
                                (size, size))
    window = pg.transform.scale(pg.image.load("window.png"),
                                (size, size))
    gore = pg.transform.scale(pg.image.load("goldore.png"),
                                (size, size))
    ## set up the blocks dictionary
    blocks = { SKY:sky, BLOCK:block, RBLOCK:rblock, GROUND:ground,
               BACKG:backg, PEBBL:pebbl, CORE:core, STNBACK:stnback,
                GOLD:gold, GWALL:gwall, WINDOW:window, GORE:gore}
    bn={SKY:"sky",BLOCK:"asdf",RBLOCK:"redstuff",
        GROUND:"ground",BACKG:"asdf background",
        PEBBL:"stone",CORE:"coal ore",STNBACK:"stone background",
        GOLD:"gold block",GWALL:"golden wall",WINDOW:"window",GORE:"gold ore"}

