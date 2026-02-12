"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module provides helper functions to calculate preparation,
baking, and total elapsed cooking time for a lasagna recipe.
"""

# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(minutes):
    """Calculate the bake time remaining.

    :param minutes: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).

    Subtracts the elapsed baking time from the EXPECTED_BAKE_TIME
    to determine how much longer the lasagna should stay in the oven.
    """
    return EXPECTED_BAKE_TIME - minutes


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - total preparation time (in minutes).

    Multiplies the number of layers by the PREPARATION_TIME constant
    to determine how long it takes to prepare the lasagna.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - time already spent baking.
    :return: int - total time elapsed (in minutes).

    Adds the preparation time (based on number_of_layers)
    to the elapsed baking time to compute the total time spent
    preparing and cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
