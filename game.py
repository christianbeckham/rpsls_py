from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.number_of_rounds = 3
        self.game_mode = ''
        self.game_mode_options = ['single player', 'multi player']
        self.player_one = None
        self.player_two = None

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.set_game_mode()
        self.run_player_setup()
        self.run_all_rounds()
        self.determine_game_winner()

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

    def run_player_setup(self):
        if self.game_mode == 'single player':
            self.player_one = Human()
            self.player_one.set_player_name()
            self.player_two = Computer()
        else:
            self.player_one = Human()
            self.player_one.set_player_name()
            self.player_two = Human()
            self.player_two.set_player_name()

        output = self.player_one.name + \
            ' vs. Computer' if self.game_mode == 'single player' else self.player_one.name + ' vs. ' + self.player_two.name
        print(f'\nGAME ON! {output}')

    def run_all_rounds(self):
        for index in range(self.number_of_rounds):
            print('\nROUND', index + 1)
            self.single_round()
            self.determine_round_winner()

    def single_round(self):
        self.player_one.generate_gesture()
        self.player_two.generate_gesture()

        while self.player_one.gesture.name == self.player_two.gesture.name:
            self.player_one.generate_gesture()
            self.player_two.generate_gesture()

    def determine_round_winner(self):
        if self.player_one.gesture.name in self.player_two.gesture.weakness:
            self.player_one.number_of_rounds_won += 1
        else:
            self.player_two.number_of_rounds_won += 1

    def determine_game_winner(self):
        if self.player_one.number_of_rounds_won > self.player_two.number_of_rounds_won:
            print(f'Congratulations, {self.player_one.name} has won!')
        elif self.player_one.number_of_rounds_won < self.player_two.number_of_rounds_won:
            print(f'Congratulations, {self.player_two.name} has won!')
        else:
            print(
                f'There was a tie between {self.player_one.name} and {self.player_two.name}')
