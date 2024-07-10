import pytest
from ..game_logic import check_bingo, manage_turns
from ..bingo_card_generation import generate_bingo_card, display_bingo_card

@pytest.fixture
def setup_game():
    players = {
        "player1": {
            "card": generate_bingo_card([f"Category {i}" for i in range(100)]),
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
    assert check_bingo(marked) == True, "Should detect a bingo in the first row"

    # Test column bingo
    marked = [[True, False, False, False, False],
              [True, False, False, False, False],
              [True, False, False, False, False],
              [True, False, False, False, False],
              [True, False, False, False, False]]
    assert check_bingo(marked) == True, "Should detect a bingo in the first column"

    # Test no bingo
    marked = [[True, False, False, False, True],
              [False, True, False, True, False],
              [False, False, False, False, False],
              [False, True, False, True, False],
              [True, False, False, False, True]]
    assert check_bingo(marked) == False, "Should not detect a bingo"

def test_manage_turns(monkeypatch, setup_game):
    # Mocking dependencies and user input
    from ..wikipedia_api import validate_category_from_url
    from ..user_interaction import handle_user_input_with_timeout, mark_category
    from save_data import save_game


    players, player = setup_game

    def mock_display_bingo_card(card, marked):
        pass

    def mock_handle_user_input_with_timeout(timeout=30):
        return "exit"

    monkeypatch.setattr("..bingo_card_generation.display_bingo_card", mock_display_bingo_card)
    monkeypatch.setattr("..user_interaction.handle_user_input_with_timeout", mock_handle_user_input_with_timeout)

    result = manage_turns(player, players)
    assert result == True, "Should exit the game when user inputs 'exit'"
