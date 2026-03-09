def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
   
    # grains double every square → 2^(number-1)
    return 2 ** (number - 1)


def total():
    # Total grains = sum of geometric series
    # 1 + 2 + 4 + ... + 2^63
    # Formula = 2^64 - 1
    return (2 ** 64) - 1