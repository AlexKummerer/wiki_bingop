import pytest
import bingo_card_generation
import colours 


def test_generate_bingo_card():
    # Test if the bingo card is generated with the correct number of categories
    categories = [f"Category {i}" for i in range(100)]
    card = bingo_card_generation.generate_bingo_card(categories)
    assert len(card) == 25, "Card should have 25 categories"
    assert all(
        category in categories for category in card
    ), "All categories in the card should be from the original list"

 
def test_display_bingo_card(capsys):
    # Test if the display_bingo_card function prints the card correctly
    categories = [f"Category {i}" for i in range(100)]
    card = bingo_card_generation.generate_bingo_card(categories)
    print(card)
    marked = [[False] * 5 for _ in range(5)]
    bingo_card_generation.display_bingo_card(card, marked)
    captured = capsys.readouterr()
    assert f"{colours.YELLOW}Bingo Card:{colours.RESET}" in captured.out, "Bingo Card header should be printed"
    assert (
        f"[ ] {card[0]}" in captured.out
    ), "Unmarked category should be displayed with [ ]"

    # Test with a marked card
    marked[0][0] = True
    bingo_card_generation.display_bingo_card(card, marked)
    captured = capsys.readouterr()
    assert (
        f"{colours.YELLOW}[X] {card[0]}{colours.RESET}" in captured.out
    ), "Marked category should be displayed with [X]"
