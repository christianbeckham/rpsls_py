from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def generate_gesture(self):
        print('Please select a gesture from the following options:')
        for index, gesture in enumerate(self.gesture_options):
            print(f'{index + 1} - {gesture}')
        user_selection = self.get_valid_gesture()
        self.gesture = self.gesture_options[user_selection - 1]

    def set_player_name(self):
        self.name = input('Please enter a name for this player: ')

    def get_valid_gesture(self):
        valid_input = False
        while valid_input is False:
            user_selection = input('Please enter the number of the gesture to perform: ')
            if user_selection.isnumeric():
                if 1 <= int(user_selection) <= len(self.gesture_options):
                    valid_input = True
                    break
            print('Invalid input, please enter a number from the list')
        return int(user_selection)