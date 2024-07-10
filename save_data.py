import json
import os


def save_game(state, file_name="save_game.json"):
    """
    Save the game state to a file.

    Parameters:
        players (dict): Dictionary of player data.
        filename (str): Filename to save the game state (default is 'game_save.json').
    """
    with open(file_name, "w") as file:
        json.dump(state, file)
    print(f"Game state saved to {file_name}.")


def load_game(file_name="save_game.json"):
    """
    Load the game state from a file.

    Parameters:
        filename (str): Filename to load the game state (default is 'game_save.json').

    Returns:
        dict: Dictionary of player data or None if no save file is found.
    """
    if not os.path.exists(file_name):
        print(f"No save file found at {file_name}")
        return None
    with open(file_name, "r") as file:
        state = json.load(file)
    print(f"Game state loaded from {file_name}.")
    return state
