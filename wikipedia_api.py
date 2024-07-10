from urllib.parse import unquote, urlparse

import wikipedia


def get_random_categories(num_categories):
    """
    Fetches a specified number of unique categories from random Wikipedia pages.

    Parameters:
    num_categories (int): The number of unique categories to fetch.

    Returns:
    list: A list containing the fetched categories.
    """
    categories = set()
    while len(categories) < num_categories:
        try:
            page_title = wikipedia.random(pages=1)
            page = wikipedia.page(title=page_title, auto_suggest=False)
            for category in page.categories:
                if len(categories) < num_categories:
                    categories.add(category)
                else:
                    break
        except wikipedia.exceptions.PageError:
            print(f"The page '{page_title}' does not exist.")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"The page '{page_title}' is a disambiguation page. Skipping...")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    return list(categories)


def extract_title_from_url(url):
    """
    Extracts the title from a Wikipedia URL.

    Parameters:
    url (str): The Wikipedia URL.

    Returns:
    str: The extracted title.
    """
    path = urlparse(url).path
    title = unquote(path.split("/")[-1])
    print(title)
    return title


def get_page_categories(title):
    """
    Fetches the categories for a given Wikipedia page title.

    Parameters:
    title (str): The Wikipedia page title.

    Returns:
    list: A list of categories if the page exists.
    str: An error message if an error occurs.
    """
    try:
        page = wikipedia.page(title=title, auto_suggest=False)
        return page.categories
    except wikipedia.exceptions.PageError:
        return f"The page '{title}' does not exist."
    except wikipedia.exceptions.DisambiguationError as e:
        return f"The page '{title}' is a disambiguation page. Possible options: {e.options}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


def set_wikipedia_language(url):
    """
    Sets the Wikipedia language based on the URL.

    Parameters:
    url (str): The Wikipedia URL.
    """
    language = urlparse(url).netloc.split(".")[0]
    wikipedia.set_lang(language)


def validate_category_from_url(url, bingo_df):
    """
    Validates if any category from the Wikipedia page exists in the bingo DataFrame.

    Parameters:
    url (str): The Wikipedia URL.
    bingo_df (pd.DataFrame): The DataFrame containing bingo categories.

    Returns:
    tuple: A tuple containing a boolean indicating validity and the found category
    or a list of    found categories.
    """
    title = extract_title_from_url(url)
    set_wikipedia_language(url)
    categories = get_page_categories(title)
    founded_categories = set()
    if isinstance(categories, str):
        return False, categories

    for category in categories:
        if category in bingo_df:
            founded_categories.add(category)

    if founded_categories:
        return True, list(founded_categories)
    return False, categories
