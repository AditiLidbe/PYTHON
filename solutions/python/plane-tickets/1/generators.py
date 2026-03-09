def generate_seat_letters(number):
    """Generate repeating seat letters A-D."""
    letters = ["A", "B", "C", "D"]
    for i in range(number):
        yield letters[i % 4]


def generate_seats(number):
    """Generate seat numbers like 1A, 1B ... skipping row 13."""
    seat_letters = generate_seat_letters(number)

    row = 1
    generated = 0

    while generated < number:
        # Skip row 13
        if row == 13:
            row += 1
            continue

        for letter in ["A", "B", "C", "D"]:
            if generated >= number:
                break
            yield f"{row}{letter}"
            generated += 1

        row += 1


def assign_seats(passengers):
    """Assign seats sequentially to passengers."""
    seats = generate_seats(len(passengers))
    return {passenger: next(seats) for passenger in passengers}


def generate_codes(seat_numbers, flight_id):
    """Generate 12-character ticket codes."""
    for seat in seat_numbers:
        base_code = seat + flight_id
        # Pad with zeros until length is 12
        yield base_code.ljust(12, "0")