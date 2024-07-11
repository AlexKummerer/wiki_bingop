import pytest
from ..bingo_card_generation import generate_bingo_card, display_bingo_card
from ..colours import PURPLE, RESET, YELLOW


def test_generate_bingo_card():
    # Test if the bingo card is generated with the correct number of categories
    categories = [f"Category {i}" for i in range(100)]
    card = generate_bingo_card(categories)
    assert len(card) == 25, "Card should have 25 categories"
    assert all(
        category in categories for category in card
    ), "All categories in the card should be from the original list"

 
def test_display_bingo_card(capsys):
    # Test if the display_bingo_card function prints the card correctly
    card = [[f"Category {i+j*5}" for i in range(5)] for j in range(5)]
    marked = [[False] * 5 for _ in range(5)]
    display_bingo_card(card, marked)
    captured = capsys.readouterr()
    assert "Wiki Bingo Card:" in captured.out, "Bingo Card header should be printed"
    assert (
        f"[ ] Category 0" in captured.out
    ), "Unmarked category should be displayed with [ ]"

    # Test with a marked card
    marked[0][0] = True
    display_bingo_card(card, marked)
    captured = capsys.readouterr()
    assert (
        f"{YELLOW}[X] Category 0{RESET}" in captured.out
    ), "Marked category should be displayed with [X]"
