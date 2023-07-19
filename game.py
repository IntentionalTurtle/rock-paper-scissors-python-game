class rps():
    def __init__(self):
        self.gameflag = True
        self.int_choice_dict = {
            1: 'Rock',
            2: 'Paper',
            3: 'Scissors'
        }
        self.str_choice_dict = {
            'rock': 1,
            'paper': 2,
            'scissors': 3
        }
        self.game()

    def game(self):
        import random
        while self.gameflag == True:
            comp_int = random.randint(1,3)
            player_choice = input("Rock, Paper, or Scissors? You may also enter 'I quit' to end.\n")
            if player_choice.lower() == 'i quit' or player_choice.lower() == 'quit' or player_choice.lower() == 'iquit':
                self.gameflag = False
                print('Thank you for playing!')
            if player_choice.lower() == 'rock' or player_choice.lower() == 'paper' or player_choice.lower() == 'scissors':
                player_int = self.str_choice_dict[player_choice.lower()]
                self.compareChoice(player_int, comp_int)
                # print('Checkpoint')
            else:
                print('Please input either Rock, Paper, Scissors, or "I quit"')

    def compareChoice(self, player, comp):
        if player == comp:
            print(f'Game Tied! Player:{self.int_choice_dict[player].title()} Computer: {self.int_choice_dict[comp].title()}')
        elif player - comp == 1 or player - comp == -2:
            print(f'You Win! Player:{self.int_choice_dict[player].title()} Computer: {self.int_choice_dict[comp].title()}')
        else:
            print(f'You Lose! Player:{self.int_choice_dict[player].title()} Computer: {self.int_choice_dict[comp].title()}')


rps()