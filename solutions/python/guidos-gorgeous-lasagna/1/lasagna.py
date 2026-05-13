"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the expected preparation time.

    Parameters:
        number_of_layers (int): The number of layers in lasagna.

    Returns:
        int: The expected preparation time for the lasagna based on the preparation time per layer.

    Function that takes the number of layers in a lasagna as an argument
    and returns the preparation time required based on the 'PREPARATION_TIME' per layer.
    """

    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the total elapsed cooking time.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total elapsed cooking time (in minutes).

    Function that takes the current elapsed time and adds it to the lasagna
    preparation time to return the total elapsed time.
    """
    
    return elapsed_bake_time + (number_of_layers * PREPARATION_TIME)
