from gesture import Gesture

class Player:
    def __init__(self):
        self.name = ''
        self.number_of_rounds_won = 0
        self.gesture = None
        self.gesture_options = self.initialize_gestures()

    def generate_gesture(self):
        pass

    def initialize_gestures(self):
        return [Gesture(name) for name in ['rock', 'paper', 'scissors', 'lizard', 'spock']]
