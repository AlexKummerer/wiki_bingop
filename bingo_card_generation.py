import random
import textwrap
import colours

def generate_bingo_card(all_categories, size=5):
    """
    Generate a bingo card from a list of categories.

    Parameters:
        categories (list): List of categories.
        size (int): Size of the bingo card (default is 5).

    Returns:
        list: Bingo card as a list.
    """
    return random.sample(all_categories, size**2)


def display_bingo_card(card, marked, size=5):
    """
    Displays the bingo card with marked categories.

    Parameters:
    card (list): A list of categories on the bingo card.
    marked (list): A 2D list of booleans representing marked categories.
    size (int): The size of the bingo card (default is 5x5).
    """
    column_width = 20  # Adjust column width based on the longest category

    print(f"{colours.YELLOW}Bingo Card:{colours.RESET}")
    for i in range(size):
        row_lines = ['' for _ in range(size)]
        for j in range(size):
            category = card[i * size + j]
            wrapped_category = textwrap.wrap(category, column_width)
            if marked[i][j]:
                wrapped_category[
                    0] = f"{colours.YELLOW}[X] {wrapped_category[0]}{colours.RESET}"
            else:
                wrapped_category[0] = f"[ ] {wrapped_category[0]}"

            for k in range(len(wrapped_category)):
                row_lines[
                    k] += f"{wrapped_category[k]:<{column_width + 4}}{colours.PURPLE}| {colours.RESET}"

            for k in range(len(wrapped_category), size):
                row_lines[k] += f"{' ' * (column_width + 4)}{colours.PURPLE} | {colours.RESET}"

        for line in row_lines:
            print(line)
        print(f"{colours.PURPLE}-{colours.RESET}" * (column_width * size + 3 * (size - 1)))
