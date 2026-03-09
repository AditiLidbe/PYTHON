def is_armstrong_number(number):
    # Convert number to string to extract digits
    digits = str(number)
    power = len(digits)

    total = 0
    for digit in digits:
        total += int(digit) ** power

    return total == number
