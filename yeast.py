"""
A class library to represent yeast in a mutualism model.
"""

import random
WORLD_SIZE = 200
class Yeast(object):
    def __init__(self, spore_prob, location):
        #Sporulation efficiency is how quickly and what percentage of yeast sporulate/are more prone to sporulation and therefore are more likely to be picked up by a fly but have slower vegetative growth
        if spore_prob < 0:
            spore_prob = 0
        self.spore_prob = spore_prob
        self.is_spore = False
        self.location = location

    def update(self):
        if self.is_spore:
            #Do nothing
            return
        if random.random() < self.spore_prob:
            #Sporulate
            self.is_spore = True
            return
        #Grow
        if not self.is_spore:
            if random.random() < .5:
                child_loc = self.location + random.randint(-1,1)
                if child_loc >= WORLD_SIZE:
                    child_loc = child_loc - WORLD_SIZE
                elif child_loc < 0:
                    child_loc = WORLD_SIZE + child_loc
                child = Yeast(random.gauss(self.spore_prob, .1), child_loc)
                return child

