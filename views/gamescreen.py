'''
Created on 10.01.2018

@author: ZuberBo
'''
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, Background
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, \
    InvalidFields
import sys
import re
import datetime
import logging
from random import choice
from models.config import Config
from models.player import Player
from models.excercise import Excercise
from models.game import Game

class GameScreenFrame(Frame):

    def __init__(self, screen, game):
        self.game = game
        super(GameScreenFrame, self).__init__(screen,
                                                int(screen.height *2 // 3),
                                                int(screen.width * 2 // 3),
                                                data={},
                                                on_load=self._reload,
                                                has_shadow=True,
                                                name="GameScreen")
        layout = Layout([1, 18, 1])
        self.add_layout(layout)
        layout.add_widget(Divider(height=3), 1)
        layout.add_widget(Label("Murphy Man 1"), 1)
        layout.add_widget(Divider(height=3), 1)
        layout2 = Layout([1, 5, 2, 11, 1])
        self.add_layout(layout2)
        self._question_widget = Text(name = "question")
        self._question_widget.disabled = True
        layout2.add_widget(self._question_widget, 1)
        self._answer_widget = Text(name = "answer")
        layout2.add_widget(self._answer_widget, 2)
        self._check_button = Button("Prüfen",self._check_answer)
        layout2.add_widget(self._check_button,3)
        layout3 = Layout([1, 18, 1])
        self.add_layout(layout3)
        layout3.add_widget(Divider(height=3), 1)
        nameWidget = Text(label="Name:",
                         name="playerName")
        nameWidget.disabled = True
        layout3.add_widget(nameWidget, 1)
        pointsWidget = Text(label="Punkte:",
            name="points")
        pointsWidget.disabled = True
        layout3.add_widget(pointsWidget, 1)
        layout3.add_widget(Divider(height=3), 1)
        layout4 = Layout([1, 1])
        self.add_layout(layout4)
        layout4.add_widget(Button("Weiter", self._reload), 0)
        layout4.add_widget(Button("Beenden", self._quit), 1)
        self.fix()

    def _check_answer(self):
        self.save()
        for key, value in self.data.items():
            if key == "answer":
                if value == str(self._excercise.result):
                    self._excercise.solved = True
                    self.game.player.addPoints(1)
                    self.game.save()
                    self._scene.add_effect(
                        PopUpDialog(self._screen,
                                    "Richtig!",
                                    ["Weiter"],
                                    on_close=self._next_round))
                    
                else:
                    self._scene.add_effect(
                        PopUpDialog(self._screen,
                                    "Falsch!",
                                    ["Neuer Versuch"],
                                    on_close=self._again))
    
    def _on_change(self):
        self.save()

    def _reload(self):
        try:
            if self._excercise.solved == True:                
                self._excercise = Excercise(choice(self.game.config.getNumberList()))
        except AttributeError:
            self._excercise = Excercise(choice(self.game.config.getNumberList()))
        self.data = {"playerName": self.game.player.name,
            "points": str(self.game.player.points),
            "question": str(self._excercise.a)+" * "+str(self._excercise.b)+" =",
            "answer": ""}

    def _quit(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Wirklich beenden?",
                        ["Ja", "Nein"],
                        on_close=self._quit_on_yes))

    @staticmethod
    def _quit_on_yes(selected):
        if selected == 0:
            raise StopApplication("Spiel beendet")
        
    @staticmethod
    def _next_round(selected):
        if selected == 0:
            raise NextScene("Game")

    @staticmethod
    def _again(selected):
        if selected == 0:
            raise NextScene("Game")
