from lib.functions import (bot_round, bot_wins, clear_terminal, head, 
                           line, name, player, player_round, player_wins,
                           tic_tac_toe, time, verify, welcome_player)

# Main code

welcome_player()  # Welcome screen
name_player = name('Your name: ').title().strip()  # Get player's name
chosen = player()   # Let the player decice which one to play
print(f'{name_player} has chose: {chosen}')  # Shows name and choice in an f_string
bot = verify(chosen)    # If player choose one option, bot got another
print(f'Bot got: {bot}')    # Shows bot's choice
clear_terminal()
matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # List with 9 numbers

# Main Looping

while True:
    tic_tac_toe(matrix)  # Function to shows a 3x3 matrix
    time.sleep(1.5)
    player_round(matrix, chosen, name_player)  # Call another function to get number and add to matrix

    for seconds in range(3):
        print('Bot is choosing.', end='\r')
        time.sleep(0.2)
        print('Bot is choosing..', end='\r')
        time.sleep(0.2)
        print('Bot is choosing...', end='\r')
        time.sleep(0.2)
        print('Bot is choosing   ', end='\r')
        time.sleep(0.2)

    if player_wins(matrix, chosen):
        clear_terminal()
        tic_tac_toe(matrix)
        head(f'{name_player} Wins')
        break

    bot_round(matrix, bot)  # Do the same thing that function above, except get number
    if bot_wins(matrix, bot):
        clear_terminal()
        tic_tac_toe(matrix)
        print(line())
        print('YOU LOSE'.center(42))
        print(line())
        break
