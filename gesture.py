class Gesture:
    def __init__(self, name):
        self.name = name.lower()
        self.weakness = self.get_weakness()

    def get_weakness(self):
        if self.name == 'rock':
            return ['paper', 'spock']
        elif self.name == 'paper':
            return ['scissors', 'lizard']
        elif self.name == 'scissors':
            return ['rock', 'spock']
        elif self.name == 'lizard':
            return ['scissors', 'rock']
        elif self.name == 'spock':
            return ['lizard', 'paper']
