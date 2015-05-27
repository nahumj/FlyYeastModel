"""
A class library to represent yeast in a mutualism model.
"""

class Yeast(object):
    def __init__(self):
        #Sporulation efficiency is how quickly and what percentage of yeast sporulate/are more prone to sporulation and therefore are more likely to be picked up by a fly but have slower vegetative growth
        self.spore_prob = .5

    def update(self):
        
        #check if sporulate
        #if didn't sporulate, try to grow
        #if did sporulate, chill out
        pass
