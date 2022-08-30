from gesture import Gesture

class Banana(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'banana'
        self.weakness = ['lizard', 'scissors', 'rock']