"""
A representation of the world for a fly and yeast simulation.
"""

from fly import Fly
from yeast import Yeast

num_fly = 10
num_yeast_col = 10

fly_pop = []
for i in range(num_fly):
    fly_pop.append(Fly())

yeast_pop = []
fori in range(num_yeast_col):
    yeast_pop.append(Yeast())

def update():
    #loop through yeast and let them try to sporulate or grow
    #if yeast grows, sporulation probability mutated

    #loop through flies and let them move
    #if fly moves to patch with yeast, gets energy and any spores that are there
    #if fly reaches enough energy, reproduces
    #if fly already had spores in it and lands in patch with room, spores hatch to yeast in that patch
    pass

for i in range(100):
    update()
