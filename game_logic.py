import save_data 
import wikipedia_api 
import bingo_card_generation 
import user_interaction 


def check_bingo(marked):
    """
    Check if the player has achieved Bingo.

    Parameters:
        card (list): Bingo card as a list of lists.
        marked (list): List of marked categories.

    Returns:
        bool: True if Bingo is achieved, False otherwise.
    """
    full_bingo = len(marked)

    # check the rows to see if spots are marked
    for row in marked:
        if all(row):
            return True

    # check the columns to see if spots are marked
    for col in range(full_bingo):
        if all(marked[row][col] for row in range(full_bingo)):
            return True

    # Check the diagonals to see if spots are marked
    if all(marked[i][i] for i in range(full_bingo)) or all(
        marked[i][full_bingo - 1 - i] for i in range(full_bingo)
    ):
        return True

    return False


def handle_players_turn(players, player_names):
    """
    Handle the sequence of turns for all players until the game ends.

    Parameters:
        players (dict): Dictionary containing player data, including their bingo cards and marked categories.
        player_names (list): List of player names.
    """
    current_player_index = 0
    num_players = len(player_names)

    while True:
        current_player = player_names[current_player_index]
        if manage_turns(current_player, players):
            break

        current_player_index = (current_player_index + 1) % num_players


def manage_turns(player, players):
    """
    Manage the turn for a single player, including marking categories and checking for bingo.

    Parameters:
        player (str): The current player's name.
        players (dict): Dictionary containing player data, including their bingo cards and marked categories.

    Returns:
        bool: True if the game ends (either a player wins or exits), otherwise None.
    """
    print(f"{player}'s turn:")
    bingo_card_generation.display_bingo_card(players[player]['card'], players[player]['marked'])
    print("Pls press Enter if you didn't see an input")
    action = user_interaction.handle_user_input_with_timeout(60)
    if action == 'exit':
        print("\033[91mThanks for playing!\033[0m")
        return True
    elif action == 'save':
        save_data.save_game(players)

    valid, categories = wikipedia_api.validate_category_from_url(action,
                                                   players[player]['card'])

    if valid:
        user_interaction.mark_category(players[player]['card'], players[player]['marked'],
                      categories)
        print("\033[94mArticle marked on the bingo card.\033[0m")
        if check_bingo(players[player]['marked']):
            print(f"{player} has won the game!")
            return True
    else:
        print(
            f"\033[91mThe article at '{action}' doesn't contain any matching categories on your bingo card.\033[0m"
        )
    return None
