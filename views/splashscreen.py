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
from models.config import Config
from models.player import Player
from models.game import Game

class SplashScreenFrame(Frame):

    def __init__(self, screen, game):
        self.game = game
        self.form_data = {
            "playerName": "",
            "cb_one": False,
            "cb_two": False,
            "cb_three": False,
            "cb_four": False,
            "cb_five": False,
            "cb_six": False,
            "cb_seven": False,
            "cb_eight": False,
            "cb_nine": False,
            "cb_ten": False
        }
        self._readConfig(game.config)
        super(SplashScreenFrame, self).__init__(screen,
                                                int(screen.height *2 // 3),
                                                int(screen.width * 2 // 3),
                                                data=self.form_data,
                                                has_shadow=True,
                                                name="SplashScreen")
        
        layout = Layout([1, 18, 1])
        self.add_layout(layout)
        self._reset_button = Button("Reset", self._reset)
        layout.add_widget(Divider(height=3), 1)
        layout.add_widget(Label("MURPHY MAN 1 - Das kleine Einmaleins"), 1)
        layout.add_widget(Divider(height=3), 1)
        layout.add_widget( CheckBox("1", "1x?", "cb_one", self._on_change), 1)
        layout.add_widget( CheckBox("2", None, "cb_two", self._on_change), 1)
        layout.add_widget( CheckBox("3", None, "cb_three", self._on_change), 1)
        layout.add_widget( CheckBox("4", None, "cb_four", self._on_change), 1)
        layout.add_widget( CheckBox("5", None, "cb_five", self._on_change), 1)
        layout.add_widget( CheckBox("6", None, "cb_six", self._on_change), 1)
        layout.add_widget( CheckBox("7", None, "cb_seven", self._on_change), 1)
        layout.add_widget( CheckBox("8", None, "cb_eight", self._on_change), 1)
        layout.add_widget( CheckBox("9", None, "cb_nine", self._on_change), 1)
        layout.add_widget( CheckBox("10", None, "cb_ten", self._on_change), 1)
        layout.add_widget(Divider(height=3), 1)
        nameWidget = Text(label="Name:",
                         name="playerName",
                         on_change=self._on_change,
                         validator="^[a-zA-Z]*$")
        layout.add_widget(nameWidget, 1)
        layout.add_widget(Divider(height=3), 1)
        layout2 = Layout([1, 1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Start", self._start), 0)
        layout2.add_widget(Button("Beenden", self._quit), 1)
        self.fix()

    def _on_change(self):
        changed = False
        self.save()
        for key, value in self.data.items():
            if key not in self.form_data or self.form_data[key] != value:
                changed = True
                break
        self._reset_button.disabled = not changed

    def _reset(self):
        self.reset()
        raise NextScene()

    def _start(self):
        self.save()
        for key, value in self.data.items():
            if key == "cb_one":
                self.game.config.one = value
            if key == "cb_two":
                self.game.config.two = value
            if key == "cb_three":
                self.game.config.three = value
            if key == "cb_four":
                self.game.config.four = value
            if key == "cb_five":
                self.game.config.five = value
            if key == "cb_six":
                self.game.config.six = value
            if key == "cb_seven":
                self.game.config.seven = value
            if key == "cb_eight":
                self.game.config.eight = value
            if key == "cb_nine":
                self.game.config.nine = value
            if key == "cb_ten":
                self.game.config.ten = value
            if key == "playerName":
                self.game.config.lastPlayer = value
        self.game.config.save()
        self.game.setPlayer(self.game.config.lastPlayer)
        raise NextScene("Game")

    def _quit(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Wirklich beenden?",
                        ["Ja", "Nein"],
                        on_close=self._quit_on_yes))

    def _readConfig(self, config):
        self.form_data = {
            "playerName": config.lastPlayer,
            "cb_one": config.one,
            "cb_two": config.two,
            "cb_three": config.three,
            "cb_four": config.four,
            "cb_five": config.five,
            "cb_six": config.six,
            "cb_seven": config.seven,
            "cb_eight": config.eight,
            "cb_nine": config.nine,
            "cb_ten": config.ten
        }


    @staticmethod
    def _quit_on_yes(selected):
        # Yes is the first button
        if selected == 0:
            raise StopApplication("Spiel beendet")
