import random

CHOICES = ['rock', 'paper', 'scissors']


def get_player_choice():
    choice = input('Choose rock, paper, or scissors: ').strip().lower()
    while choice not in CHOICES:
        choice = input('Invalid choice. Choose rock, paper, or scissors: ').strip().lower()
    return choice


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(player, computer):
    if player == computer:
        return 'Draw!'
    winning_pairs = {
        ('rock', 'scissors'),
        ('paper', 'rock'),
        ('scissors', 'paper'),
    }
    if (player, computer) in winning_pairs:
        return 'You win!'
    return 'Computer wins!'


def main():
    print('Rock, Paper, Scissors Game!')
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f'Computer chose {computer_choice}')
    result = determine_winner(player_choice, computer_choice)
    print(result)


if __name__ == '__main__':
    main()
