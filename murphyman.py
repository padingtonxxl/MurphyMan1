from models.config import Config
from models.excercise import Excercise
from models.game import Game
from models.player import Player

from views.splashscreen import *
from views.gamescreen import *

from random import randint, choice
from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, Background
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, InvalidFields
import sys, os, datetime

def main(screen, scene):
    config = Config(os.getcwd() + '\murphyzahl.cfg')
    game = Game(config)
    splashScene = Scene([Background(screen), SplashScreenFrame(screen, game)], -1, name="Splash")
    gameScene = Scene([Background(screen), GameScreenFrame(screen, game)], -1, name="Game")
    scenes = [
        splashScene,
        gameScene
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=splashScene)

last_scene = None
while True:
    try:
        Screen.wrapper(main, catch_interrupt=False, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene
