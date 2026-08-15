"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME: int = 40
PREPARATION_TIME: int = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - bake_time


#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(layers: int) -> int:
    """Calculate the preparation time in minutes.

    Parameters:
        layers (int): The number of layers in the lasagna.

    Returns:
        int: The total preparation time (in minutes) based on the number of layers.

    Function that takes the number of layers as an argument and returns the total
    preparation time in minutes, based on a constant preparation time per layer.
    """
    return layers * PREPARATION_TIME


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total elapsed time in minutes.

    Parameters:
        layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total elapsed time (in minutes) based on the number of layers and the elapsed bake time.

    Function that takes the number of layers and the actual minutes the lasagna has been in the oven as arguments,
    and returns the total elapsed time in minutes.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
