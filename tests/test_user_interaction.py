import pytest
from user_interaction import mark_category, input_with_timeout, handle_user_input_with_timeout
from colours import BLUE, RED, RESET, YELLOW


def test_mark_category(capsys):
    card = [f"Category {i}" for i in range(25)]
    marked = [[False]*5 for _ in range(5)]
    categories = ["Category 0", "Category 24"]
    
    mark_category(card, marked, categories)
    captured = capsys.readouterr()

    assert marked[0][0] == True
    assert marked[4][4] == True
    assert f"{YELLOW}Category 'Category 0' marked!{RESET}" in captured.out
    assert f"{YELLOW}Category 'Category 24' marked!{RESET}" in captured.out

def test_input_with_timeout(monkeypatch):
    def mock_input(prompt):
        return 'input_test'
    monkeypatch.setattr('builtins.input', mock_input)
    result = input_with_timeout("Prompt", 1)
    assert result == 'input_test'

def test_handle_user_input_with_timeout(monkeypatch):
    def mock_input(prompt):
        return 'save'
    monkeypatch.setattr('builtins.input', mock_input)
    result = handle_user_input_with_timeout(1)
    assert result == 'save'
