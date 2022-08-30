import imp
from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock
from banana import Banana

class Player:
    def __init__(self):
        self.name = ''
        self.number_of_rounds_won = 0
        self.gesture = None
        self.gesture_options = self.initialize_gestures()

    def generate_gesture(self):
        pass

    def initialize_gestures(self):
        return [Rock(), Paper(), Scissors(), Lizard(), Spock(), Banana()]
