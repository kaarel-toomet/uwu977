# uwu977

## What it is

tile based game thingy

## Starting

Command line:

`uwu977.py`

It has various arguments, check `uwu977.py -h`.


## How to play
arrow keys to move, ASDW to build, P to pause, H to set home, R to return home,
 [ or ] to choose build block, X to toggle home visibility, Z to save world file,
 IJKL to break, C to break wall/background, G to switch gamemode

note:world has to be named "world.npz" to load


## Requirements

It is tested with python3 3.6 only but may run with python 2 too:

* python 3
* pygame
* numpy

## Issues

Currently the screen scaling does not work: I haven't found a good way
to get screen DPI.
