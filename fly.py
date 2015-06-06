"""
A class library to model fly behavior.
"""
from random import *
WORLD_SIZE = 200


class Fly(object):
    '''Doc string'''
    def __init__(self, location):
        #A list for holding the collection of yeast spores in the fly gut
        self.stomach = []
        self.location = location
        self.fitness = 0

    def move(self, yeast_pop):
        self.location += randint(0, WORLD_SIZE/4)
        if self.location >= WORLD_SIZE:
            self.location = self.location - WORLD_SIZE
        if not yeast_pop[self.location] and len(self.stomach):
            hatched = self.stomach.pop()
            hatched.is_spore = False
            yeast_pop[self.location] = hatched
        

    def eat(self, yeast):
        if yeast.is_spore:
            self.stomach.append(yeast)
        else:
            self.fitness += 1
    

    def reproduce(self):
        new_loc=round(gauss(self.location, 2),0)
        if new_loc < 0:
            new_loc = 0
        elif new_loc > WORLD_SIZE-1:
            new_loc = WORLD_SIZE-1
        #how best to keep fly location within yeast world??
        return Fly(new_loc)

    def update(self, yeast_pop):
        if yeast_pop[self.location]:
            self.eat(yeast_pop[self.location])
        if self.fitness == 10:
            return self.reproduce()
        else:
            self.move(yeast_pop)
