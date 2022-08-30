from gesture import Gesture

class Rock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'rock'
        self.weakness = ['paper', 'spock']