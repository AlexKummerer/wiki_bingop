# Wiki Bingo

Wiki Bingo is an engaging and educational multiplayer game that combines the thrill of bingo with the vast information available on Wikipedia. The objective is to complete a bingo card filled with categories by finding relevant Wikipedia articles. Players take turns entering the URLs of articles they find, and the game validates and marks the categories. The first player to complete a row, column, or diagonal wins the game.

## Features
1. **Multiplayer**: Supports multiple players with personalized bingo cards.
2. **Timed Turns**: Adds excitement and urgency to each player's turn.
3. **Wikipedia Integration**: Leverages the vast repository of Wikipedia articles and categories.
4. **Save/Load Game**: Allows players to save their progress and resume the game later.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository or download the `rps_tournament.py` file.**

2. **Create a Virtual Environment (recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install requirements:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Game

1. **Start the Game**
  ```bash
    python main.py
  ```
2. **Follow the prompts**
  - Choose whether to load a saved game or start a new game.
  - Enter the number of players.
  - Enter the name for each player.
  - Follow the on-screen instructions to play the game.
# Wiki Bingo

Wiki Bingo is an engaging and educational multiplayer game that combines the thrill of bingo with the vast information available on Wikipedia. The objective is to complete a bingo card filled with categories by finding relevant Wikipedia articles. Players take turns entering the URLs of articles they find, and the game validates and marks the categories. The first player to complete a row, column, or diagonal wins the game.

## Features
1. **Multiplayer**: Supports multiple players with personalized bingo cards.
2. **Timed Turns**: Adds excitement and urgency to each player's turn.
3. **Wikipedia Integration**: Leverages the vast repository of Wikipedia articles and categories.
4. **Save/Load Game**: Allows players to save their progress and resume the game later.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository or download the `rps_tournament.py` file.**

2. **Create a Virtual Environment (recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install requirements:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Game

1. **Start the Game**
  ```bash
    python main.py
  ```
2. **Follow the prompts**
  - Choose whether to load a saved game or start a new game.
  - Enter the number of players.
  - Enter the name for each player.
  - Follow the on-screen instructions to play the game.



## How to Play
1. **Setup**: Each player receives a unique 5x5 bingo card generated from random Wikipedia categories.

2. **Turn-Based Play**: Players take turns entering the URLs of Wikipedia articles they find.

3. **Category Validation**: The game checks if the article contains a category that matches any on the player's bingo card.

4. **Marking Categories**: Valid categories are marked on the player's bingo card.

5. **Winning**: The first player to complete a row, column, or diagonal on their bingo card wins the game.

## Rules

1. **Player Turns**: Each player has a limited amount of time (e.g., 60 seconds) to enter the URL of a Wikipedia article during their turn.

2. **URL Validation**: The URL entered by the player is used to extract the article title and validate the categories.

3. **Marking**: Only categories present on the player's bingo card can be marked.

4. **Saving and Exiting**: Players can save their progress and exit the game, resuming later from where they left off.


## Implementation

The game is implemented in Python and consists of several key components, each managed by a different developer:

1. Wikipedia API Integration
  - 1. Set up the Wekipedia API https://pypi.org/project/wikipedia/
  - 2. Fetch the catgories
  - 3. validate the categorys by url
2. Bingo Card Generation and Display
  - . gnerate a 5x5 bingo card from from a list of categories
  - 2. Display the bingo in the terminal, higlighting marked categories
3. User Interaction and Input Handling - Mohammed
  - 1. Handle user input by entering the url
  - 2. Validate the user input 
  - 3. mark the cartegories the grid  
  - 4. Time handling/ Input is processed in a given limit                                     
4. Game Logic and Turn Management
  - 1. check Bingo
  - 2. Manage turns / call handl user input and check the bingo card
5. Save/Load Game State
  - 1. Save Game State
  - 2. Load Game State
6. Integration and testing
  - 1. Unit tests
  - 2. Manuel ests

## Contriuting

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your branch.
4. Create a pull request explaining your changes.
5. Please make sure your code follows the existing style and includes appropriate tests.

## Conclusion

This repository contains the code for a Wiki Bingo game. Follow the setup instructions to install dependencies and run the game. Enjoy playing Wiki Bingo with your friends and family!
