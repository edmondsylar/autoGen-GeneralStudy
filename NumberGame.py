import os
from ModelConfigs import getAndSet_config

from autogen import ConversableAgent

# azure llm config
azure_llm_config = getAndSet_config("azure_llm_config")

# mistral llm config
mistral_llm_config = getAndSet_config("groq_llm_config_mixtral")

game_script = '''
Title: Number Guessing Game Instructions

    Introduction:
    The number guessing game is a simple two-player game that involves one player thinking of a number and the other player trying to guess it. With each failed attempt, the guesser does not earn any points. However, if they guess correctly on their first attempt, they earn 5 points, and for each subsequent attempt, the points earned decrease by 1.

    Getting Started:

    1. Decide which player will be Player 1 and which player will be Player 2.
    2. Player 1 thinks of a number between 1 and 100.
    3. Player 1 tells Player 2 that they have thought of a number.
    4. Player 2 begins guessing the number.

    Number Guessing Example:

    - Player 1 thinks of the number 35.
    - Player 1 tells Player 2 that they have thought of a number.
    - Player 2 makes their first guess, which is 50.
    - Player 1 tells Player 2 that their guess is too high.
    - Player 2 makes their second guess, which is 40.
    - Player 1 tells Player 2 that their guess is too low.
    - Player 2 makes their third guess, which is 35.
    - Player 1 tells Player 2 that their guess is correct, and Player 2 earns 3 points.

    Scoring:

    - If Player 2 guesses the number correctly on their first attempt, they earn 5 points.
    - For each subsequent attempt, the points earned decrease by 1.

    Winning the Game:

    The game ends when an agreed-upon time limit has been reached or a certain number of rounds have been played. The player with the most points at the end of the game is the winner.

'''

agent_with_number = ConversableAgent(
    "Donnah",
    system_message= f'''
    Your Name Is Donnah and you are a part of a game competition.

    # Game.
    {game_script}

    You have it in mind to go first.
    Be polite and always greet the other player.
    ''',
    llm_config=mistral_llm_config,
    is_termination_msg=lambda msg: "53" in msg["content"],  # terminate if the number is guessed by the other agent
    human_input_mode="TERMINATE",  # never ask for human input
)

agent_guess_number = ConversableAgent(
    "Ann",
    system_message= f'''
    Your Name Is Ann and you are a part of a game competition.

    # Game.
    {game_script}

    You are nice and deep logical thinker
    ''',
    llm_config=mistral_llm_config,
    human_input_mode="NEVER",
)

human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,
    human_input_mode="ALWAYS",

)

result = agent_with_number.initiate_chat(
    agent_guess_number,
    message="",
)