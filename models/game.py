'''
Created on 10.01.2018

@author: ZuberBo
'''
from models.player import Player

class Game:
    
    def __init__(self, config, playerName=None):
        self.config = config
        if playerName != None:
            self.player = Player(playerName)
        else:
            self.player = Player()
            
    def setPlayer(self, playerName):
        self.player.load(playerName)

    def save(self):
        self.player.save()
        
