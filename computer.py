from player import Player
import random


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Computer'

    def generate_gesture(self):
        self.gesture = random.choice(self.gesture_options)
        print(f'{self.name} selected {self.gesture.name}')
