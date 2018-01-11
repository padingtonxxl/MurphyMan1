'''
Created on 10.01.2018

@author: ZuberBo
'''
import os
from random import randint
class Player:

    def __init__(self, name="", path=None):
        self.load(name, path)
        self.id = randint(1,100)

    def load(self, name, path=None):
        if path == None:
            path = os.getcwd()
        self.filename = path + '\\' + name + '.cfg'
        try:
            self.playerFile = open(self.filename, 'r')
            fileLines = self.playerFile.readlines()
            for line in fileLines:
                splits = line.split( ':')
                parameter = splits[0]
                value = splits[1].rstrip("\n")
                if parameter == 'name':
                    self.name = value
                elif parameter == 'points':
                    self.points = int(value)
            self.playerFile.close()
        except FileNotFoundError:
            self.name = "tbd"
            self.points = 0

    
    def addPoints(self, points):
        self.points = self.points + points
        
    def save(self):
        self.playerFile = open(self.filename, 'w')
        self.playerFile.write('name:'+self.name+'\n')
        self.playerFile.write('points:'+str(self.points)+'\n')
        self.playerFile.close()
