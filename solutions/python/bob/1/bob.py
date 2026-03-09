def response(hey_bob):
    # Remove surrounding whitespace
    stripped = hey_bob.strip()

    # Silence
    if stripped == "":
        return "Fine. Be that way!"

    # Check if yelling (has at least one letter and all letters are uppercase)
    is_yelling = stripped.isupper()

    # Check if question
    is_question = stripped.endswith("?")

    # Yelled question
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"

    # Yelling
    if is_yelling:
        return "Whoa, chill out!"

    # Question
    if is_question:
        return "Sure."

    # Default
    return "Whatever." 