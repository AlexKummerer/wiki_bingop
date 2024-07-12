import pytest
import game_logic
import bingo_card_generation
import user_interaction

@pytest.fixture
def setup_game():
    players = {
        "player1": {
            "card": bingo_card_generation.generate_bingo_card([f"Category {i}" for i in range(100)]),
            "marked": [[False]*5 for _ in range(5)]
        }
    }
    player = "player1"
    return players, player

def test_check_bingo():
    # Test row bingo
    marked = [[True, True, True, True, True],
              [False, False, False, False, False],
              [False, False, False, False, False],
              [False, False, False, False, False],
              [False, False, False, False, False]]
    assert game_logic.check_bingo(marked) == True, "Should detect a bingo in the first row"

    # Test column bingo
    marked = [[True, False, False, False, False],
              [True, False, False, False, False],
              [True, False, False, False, False],
              [True, False, False, False, False],
              [True, False, False, False, False]]
    assert game_logic.check_bingo(marked) == True, "Should detect a bingo in the first column"

    # Test no bingo
    marked = [[True, False, False, False, True],
              [False, True, False, True, False],
              [False, False, False, False, False],
              [False, True, False, True, False],
              [True, False, False, False, True]]
    assert game_logic.check_bingo(marked) == False, "Should not detect a bingo"

def test_manage_turns(monkeypatch, setup_game):
    players, player = setup_game

    def mock_input(prompt):
        return 'exit'

    def mock_display_bingo_card(card, marked, size):
        pass

    def mock_handle_user_input_with_timeout(timeout):
        return "exit"

    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr(bingo_card_generation, 'display_bingo_card', mock_display_bingo_card)
    monkeypatch.setattr(user_interaction, 'handle_user_input_with_timeout', mock_handle_user_input_with_timeout)

    result = game_logic.manage_turns(player, players)
    assert result == True, "Should exit the game when user inputs 'exit'"
