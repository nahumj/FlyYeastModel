"""
A representation of the world for a fly and yeast simulation.
"""

from fly import Fly
from yeast import Yeast
from random import *

NUM_FLY = 10
NUM_YEAST_COL = 100
WORLD_SIZE = 200
NUM_UPDATES = 1000

FREE_YEAST_POP = [Yeast(random(), _) for _ in range(NUM_YEAST_COL)]
#Allows for empty patches
FREE_YEAST_POP = FREE_YEAST_POP + [None for _ in range(WORLD_SIZE - NUM_YEAST_COL)]

FLY_POP = [Fly(randint(0, len(FREE_YEAST_POP)-1)) for _ in range(NUM_FLY)]


def update():
    #loop through yeast and let them try to sporulate or grow
    for yeast in FREE_YEAST_POP:
        if yeast:
            result = yeast.update()
            if result:
                #baby yeast!
                FREE_YEAST_POP[result.location] = result

    #loop through flies and let them move
    for fly in FLY_POP:
        #currently having fly eat before it moves since it is easier
        result = fly.update(FREE_YEAST_POP)
        FREE_YEAST_POP[fly.location] = None
        if result is Fly:
            #baby fly!
            index = randint(0, NUM_FLY-1)
            FLY_POP[index] = result


    #if fly moves to patch with yeast, gets energy and any spores that are there
    #if fly reaches enough energy, reproduces
    #if fly already had spores in it and lands in patch with room, spores hatch to yeast in that patch

for i in range(NUM_UPDATES):
    update()

yeast_sum = 0
yeast_count = 0
for yeast in FREE_YEAST_POP:
    if yeast:
        yeast_sum += yeast.spore_prob
        yeast_count += 1

print(yeast_sum/yeast_count)
