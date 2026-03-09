def get_list_of_wagons(*wagon_ids):
    """Return a list of wagons."""
    return list(wagon_ids)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons."""

    # unpack first two wagons and the rest
    first, second, *rest = each_wagons_id

    # find locomotive (always ID 1)
    locomotive_index = rest.index(1)
   
    # rebuild list:
    # locomotive + missing wagons + remaining wagons (except locomotive) + first two at end
    fixed_list = (
        [1]
        + missing_wagons
        + rest[:locomotive_index]
        + rest[locomotive_index + 1:]
        + [first, second]
    )

    return fixed_list


def add_missing_stops(route, /, **stops):
    """Add missing stops to route dict."""

    # collect stop values in order
    route["stops"] = list(stops.values())

    return route


def extend_route_information(route, more_route_information):
    """Extend route information."""

    # dictionary unpacking
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix wagon depot layout."""

    # unpack rows
    first_row, second_row, third_row = wagons_rows

    # unpack columns (zip transpose logic manually)
    row1 = [first_row[0], second_row[0], third_row[0]]
    row2 = [first_row[1], second_row[1], third_row[1]]
    row3 = [first_row[2], second_row[2], third_row[2]]

    return [row1, row2, row3]