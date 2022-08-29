class Game:
    def __init__(self):
        self.number_of_rounds = 3
        self.game_mode = ''
        self.game_mode_options = ['single player', 'multi player']

    def display_welcome(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')

    def display_rules(self):
        print('\nRules:\nScissors cuts \nPaper covers \nRock crushes \nLizard poisons \nSpock smashes \nScissors decapitates \nLizard eats \nPaper disproves \nSpock vaporizes \nRock crushes Scissors')

    def set_game_mode(self):
        print('\nPlease select a game mode from the following options:')
        for index, mode in enumerate(self.game_mode_options):
            print(f'\t{index + 1} - {mode.title()}')
        user_selection = self.get_valid_mode()
        self.game_mode = self.game_mode_options[user_selection - 1]

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.set_game_mode()

    def get_valid_mode(self):
        valid_input = False
        while valid_input is False:
            user_selection = input(
                'Please enter the number of the mode to perform: ')
            if user_selection.isnumeric():
                if 1 <= int(user_selection) <= len(self.game_mode_options):
                    valid_input = True
                    break
            print('Invalid input, please enter a number from the list')
        return int(user_selection)
