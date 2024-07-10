from save_data import load_game
from bingo_card_generation import generate_bingo_card
from wikipedia_api import get_random_categories
from game_logic import handle_players_turn

def setup_new_game():
    """
    Set up a new game by initializing players and their bingo cards.

    Returns:
        tuple: A tuple containing the dictionary of players and the list of player names.
    """
    num_players = int(input("Enter the number of players: "))
    players = {}

    for i in range(1, num_players + 1):
        player_name = input(f"Enter name for Player {i}: ")
        players[player_name] = {}

    categories = get_random_categories(num_players * 25)
    for player in players:
        player_categories = categories[:25]
        categories = categories[25:]
        players[player]["card"] = generate_bingo_card(player_categories)
        players[player]["marked"] = [[False] * 5 for _ in range(5)]

    player_names = list(players.keys())
    return players, player_names


def main():
    """
    Main function to start the Wiki Bingo game.
    """
    print("Welcome to Wiki Bingo!\n")

    # Greet users and ask if they want to load a saved game or start a new game
    load_choice = (
        input("Do you want to load the saved game? (yes/no): ").strip().lower()
    )

    if load_choice == "yes":
        players = load_game()
        if players:
            print("Game loaded successfully!")
            player_names = list(players.keys())
        else:
            print("No saved game found. Starting a new game.")
            players, player_names = setup_new_game()
    else:
        players, player_names = setup_new_game()

    print(
        "Instructions: Find Wikipedia articles that match the categories on your bingo card."
    )
    print("Enter the URL of the article you found to mark it on your card.")
    print("Type 'save' to save your progress or 'exit' to quit the game.")

    handle_players_turn(players, player_names)


if __name__ == "__main__":
    main()
