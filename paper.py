from gesture import Gesture

class Paper(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'paper'
        self.weakness = ['scissors', 'lizard', 'banana']