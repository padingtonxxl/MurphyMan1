'''
Created on 10.01.2018

@author: ZuberBo
'''

from random import randint

class Excercise:
    def __init__(self, b=randint(2,10)):
        self.a = randint(2,10)
        self.b = b
        self.operator = '*'
        self.result = str(self.a * self.b)
        self.solved = False