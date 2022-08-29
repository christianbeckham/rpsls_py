from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.number_of_rounds = 3
        self.game_mode = ''
        self.game_mode_options = ['single player', 'multi player']
        self.players = []

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
        self.run_player_setup()
        self.run_all_rounds()
        self.determine_game_winner()

    def run_player_setup(self):
        if self.game_mode == 'single player':
            human_one = Human()
            human_one.set_player_name()
            self.players.extend([human_one, Computer()])
        else:
            human_one = Human()
            human_one.set_player_name()
            human_two = Human()
            human_two.set_player_name()
            self.players.extend([human_one, human_two])

        output = self.players[0].name + \
            ' vs. Computer' if self.game_mode == 'single player' else self.players[
                0].name + ' vs. ' + self.players[1].name
        print(f'\nGAME ON! {output}')

    def run_all_rounds(self):
        for index in range(self.number_of_rounds):
            print('\nROUND', index + 1)
            self.single_round()
            self.determine_round_winner()

    def determine_game_winner(self):
        if self.players[0].number_of_rounds_won > self.players[1].number_of_rounds_won:
            print(f'Congratulations, {self.players[0].name} has won!')
        elif self.players[0].number_of_rounds_won < self.players[1].number_of_rounds_won:
            print(f'Congratulations, {self.players[1].name} has won!')
        else:
            print(
                f'There was a tie between {self.players[0].name} and {self.players[1].name}')

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

    def determine_round_winner(self):
        if self.players[0].gesture == 'rock' and self.players[1].gesture in ['scissors', 'lizard']:
            self.players[0].number_of_rounds_won += 1
        elif self.players[0].gesture == 'paper' and self.players[1].gesture in ['rock', 'spock']:
            self.players[0].number_of_rounds_won += 1
        elif self.players[0].gesture == 'scissors' and self.players[1].gesture in ['paper', 'lizard']:
            self.players[0].number_of_rounds_won += 1
        elif self.players[0].gesture == 'lizard' and self.players[1].gesture in ['spock', 'paper']:
            self.players[0].number_of_rounds_won += 1
        elif self.players[0].gesture == 'spock' and self.players[1].gesture in ['scissors', 'rock']:
            self.players[0].number_of_rounds_won += 1
        else:
            self.players[1].number_of_rounds_won += 1

    def single_round(self):
        self.players[0].generate_gesture()
        self.players[1].generate_gesture()

        while self.players[0].gesture == self.players[1].gesture:
            self.players[0].generate_gesture()
            self.players[1].generate_gesture()
