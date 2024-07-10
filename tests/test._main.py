import pytest
from ..main import setup_new_game, main

def test_setup_new_game(monkeypatch):
    inputs = iter(['2', 'Alice', 'Bob'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    players, player_names = setup_new_game()
    assert len(players) == 2
    assert 'Alice' in players
    assert 'Bob' in players
    assert len(player_names) == 2

def test_main(monkeypatch):
    def mock_input(prompt):
        return 'no'

    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr('project.main.setup_new_game', lambda: ({}, []))
    monkeypatch.setattr('project.main.handle_players_turn', lambda players, names: None)

    main()
