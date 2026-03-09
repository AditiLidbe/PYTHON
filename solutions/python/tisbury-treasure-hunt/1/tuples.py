def get_coordinate(record):
    """Return coordinate value from a (treasure, coordinate) pair."""
    return record[1]


# TASK 2
def convert_coordinate(coordinate):
    """
    Convert coordinate from format "2A"
    into tuple format ("2", "A")
    """
    return (coordinate[0], coordinate[1])


# TASK 3
def compare_records(azara_record, rui_record):
    """
    Compare coordinates from Azara and Rui.
    Return True if they match, else False.
    """
    azara_coord = convert_coordinate(azara_record[1])
    rui_coord = rui_record[1]

    return azara_coord == rui_coord


# TASK 4
def create_record(azara_record, rui_record):
    """
    Return combined record if coordinates match.
    Else return "not a match".
    """
    if compare_records(azara_record, rui_record):
        return (
            azara_record[0],        # treasure
            azara_record[1],        # original coordinate string
            rui_record[0],          # location
            rui_record[1],          # coordinate tuple
            rui_record[2]           # quadrant
        )
    else:
        return "not a match"


# TASK 5
def clean_up(combined_record_group):
    """
    Remove duplicate coordinate and return formatted multi-line string.
    """
    report = ""

    for record in combined_record_group:
        cleaned_record = (
            record[0],  # treasure
            record[2],  # location
            record[3],  # coordinate tuple
            record[4]   # quadrant
        )

        report += str(cleaned_record) + "\n"

    return report