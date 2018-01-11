'''
Created on 10.01.2018

@author: ZuberBo
'''
class Config:
    def __init__(self, filename):
        self._filename = filename
        self.initValues()
        self.configFile = open(self._filename, 'r')
        fileLines = self.configFile.readlines()
        for line in fileLines:
            splits = line.split( ':')
            parameter = splits[0]
            value = splits[1].rstrip('\n')
            if parameter == 'window.width':
                self.windowWidth = int(value)
            elif parameter == 'window.height':
                self.windowHeight = int(value)
            elif parameter == 'game.lastplayer':
                self.lastPlayer = value
            elif parameter == 'game.one':
                self.one = value == "True"
            elif parameter == 'game.two':
                self.two = value == "True"
            elif parameter == 'game.three':
                self.three = value == "True"
            elif parameter == 'game.four':
                self.four = value == "True"
            elif parameter == 'game.five':
                self.five = value == "True"
            elif parameter == 'game.six':
                self.six = value == "True"
            elif parameter == 'game.seven':
                self.seven = value == "True"
            elif parameter == 'game.eight':
                self.eight = value == "True"
            elif parameter == 'game.nine':
                self.nine = value == "True"
            elif parameter == 'game.ten':
                self.ten = value == "True"
        self.configFile.close()

    def getNumberList(self):
        numberList = []
        if self.one:
            numberList.append(1)
        if self.two:
            numberList.append(2)
        if self.three:
            numberList.append(3)
        if self.four:
            numberList.append(4)
        if self.five:
            numberList.append(5)
        if self.six:
            numberList.append(6)
        if self.seven:
            numberList.append(7)
        if self.eight:
            numberList.append(8)
        if self.nine:
            numberList.append(9)
        if self.ten:
            numberList.append(10)
        return numberList

    def save(self):
        self.configFile = open(self._filename, 'w')
        self.configFile.write('window.width:'+str(self.windowWidth)+'\n')
        self.configFile.write('window.height:'+str(self.windowHeight)+'\n')
        self.configFile.write('game.lastplayer:'+str(self.lastPlayer)+'\n')
        self.configFile.write('game.one:'+str(self.one)+'\n')
        self.configFile.write('game.two:'+str(self.two)+'\n')
        self.configFile.write('game.three:'+str(self.three)+'\n')
        self.configFile.write('game.four:'+str(self.four)+'\n')
        self.configFile.write('game.five:'+str(self.five)+'\n')
        self.configFile.write('game.six:'+str(self.six)+'\n')
        self.configFile.write('game.seven:'+str(self.seven)+'\n')
        self.configFile.write('game.eight:'+str(self.eight)+'\n')
        self.configFile.write('game.nine:'+str(self.nine)+'\n')
        self.configFile.write('game.ten:'+str(self.ten)+'\n')
        self.configFile.close()

    def initValues(self):
        self.windowWidth = 65
        self.windowHeight = 30
        self.lastPlayer = ""
        self.one=False
        self.two=False
        self.three=False
        self.four=False
        self.five=False
        self.six=False
        self.seven=False
        self.eight=False
        self.nine=False
        self.ten=False
