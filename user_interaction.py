import threading
from colours import BLUE, RED, RESET, YELLOW


def mark_category(bingo_card, marked_categories, categories):
    """
    Mark categories on the bingo card.

    Parameters:
        bingo_card (list): Bingo card as a list of lists.
        marked_categories (list): List of marked categories.
        categories (list): List of categories to mark.
    """

    size = len(marked_categories)

    for category in categories:
        found = False
        for row in range(size):
            for column in range(len(marked_categories[row])):
                bingo_category = bingo_card[row * size + column]
                if bingo_category.lower() == category.lower():
                    if not marked_categories[row][column]:
                        marked_categories[row][column] = True
                        print(f"{YELLOW}Category '{category}' marked!{RESET}")
                    else:
                        print(f"{BLUE}Category '{category}' is already marked!{RESET}")
                    found = True
                    break
            if found:
                break
        if not found:
            print(
                f"{RED}Category '{category}' from the article is not on the bingo card{RESET}"
            )


def input_with_timeout(prompt, timeout):
    """
    Get user input with a timeout.

    Parameters:
        prompt (str): Prompt to display.
        timeout (int): Timeout in seconds.

    Returns:
        str: User input or empty string if timeout.
    """

    def timed_input():
        nonlocal user_input
        user_input = input(prompt)
        input_received.set()

    user_input = ""
    input_received = threading.Event()

    input_thread = threading.Thread(target=timed_input)
    input_thread.start()

    input_thread.join(timeout)

    if input_received.is_set():
        return user_input
    else:
        return user_input


def handle_user_input_with_timeout(timeout=30):
    """
    Handle user input with a timeout.

    Args:
        timeout (int): Timeout in seconds.

    Returns:
        str: User input or empty string if timeout.
    """
    timeout_in_seconds = timeout
    prompt = f"Enter a Wikipedia URL (or type 'save' to save, 'exit' to exit) within {timeout_in_seconds} seconds: "
    user_input = input_with_timeout(prompt, timeout_in_seconds)
    if user_input:
        return user_input
    else:
        print(f"{RED}Time's up! Input session expired.{RESET}")
        return user_input
