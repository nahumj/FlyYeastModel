"""
A representation of the world for a fly and yeast simulation.
"""

from fly import Fly
from yeast import Yeast

NUM_FLY = 10
NUM_YEAST_COL = 10
NUM_UPDATES = 100

fly_pop = [Fly() for _ in range(NUM_FLY)]

yeast_pop = [Yeast() for _ in range(NUM_YEAST_COL)]

def update():
    #loop through yeast and let them try to sporulate or grow
    #if yeast grows, sporulation probability mutated

    #loop through flies and let them move
    #if fly moves to patch with yeast, gets energy and any spores that are there
    #if fly reaches enough energy, reproduces
    #if fly already had spores in it and lands in patch with room, spores hatch to yeast in that patch
    pass

for i in range(NUM_UPDATES):
    update()
