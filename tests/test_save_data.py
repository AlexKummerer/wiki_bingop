import pytest
import json
from ..save_data import save_game, load_game

def test_save_game(tmp_path):
    state = {'player1': {'card': [], 'marked': []}}
    file_path = tmp_path / "save_game.json"
    save_game(state, file_name=file_path)
    assert file_path.exists()

    with open(file_path, "r") as file:
        loaded_state = json.load(file)
    assert loaded_state == state

def test_load_game(tmp_path):
    state = {'player1': {'card': [], 'marked': []}}
    file_path = tmp_path / "save_game.json"
    with open(file_path, "w") as file:
        json.dump(state, file)
    
    loaded_state = load_game(file_name=file_path)
    assert loaded_state == state
