from human import Human
from computer import Computer

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
        players = self.run_player_setup()
        self.run_all_rounds(players)
        self.determine_game_winner(players)

    def run_player_setup(self):
        players = []
        if self.game_mode == 'single player':
            human_one = Human()
            human_one.set_player_name()
            players.extend([human_one, Computer()])
        else:
            human_one = Human()
            human_one.set_player_name()
            human_two = Human()
            human_two.set_player_name()
            players.extend([human_one, human_two])
        for player in players:
            print(f'Welcome {player.name}!')
        return players
            
    def run_all_rounds(self, players):
        for _ in range(self.number_of_rounds):
            players[0].generate_gesture()
            players[1].generate_gesture()
            if players[0].gesture != players[1].gesture:
                self.determine_round_winner(players)

    def determine_game_winner(self, players):
        if players[0].number_of_rounds_won > players[1].number_of_rounds_won:
            print(f'Congratulations, {players[0].name} has won!')
        elif players[0].number_of_rounds_won > players[1].number_of_rounds_won:
            print(f'Congratulations, {players[1].name} has won!')
        else:
            print(f'There was a tie between {players[0].name} and {players[1].name}')
        

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

    def determine_round_winner(self, players):
        if players[0].gesture == 'rock' and players[1].gesture in ['scissors', 'lizard']:
            players[0].number_of_rounds_won += 1
        elif players[0].gesture == 'paper' and players[1].gesture in ['rock', 'spock']:
            players[0].number_of_rounds_won += 1
        elif players[0].gesture == 'scissors' and players[1].gesture in ['paper', 'lizard']:
            players[0].number_of_rounds_won += 1
        elif players[0].gesture == 'lizard' and players[1].gesture in ['spock', 'paper']:
            players[0].number_of_rounds_won += 1
        elif players[0].gesture == 'spock' and players[1].gesture in ['scissors', 'rock']:
            players[0].number_of_rounds_won += 1
        else:
            players[1].number_of_rounds_won += 1