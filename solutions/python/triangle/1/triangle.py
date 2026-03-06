def equilateral(sides):
    # Check triangle validity first
    a, b, c = sides
    if not _is_valid_triangle(a, b, c):
        return False
    return a == b == c


def isosceles(sides):
    a, b, c = sides
    if not _is_valid_triangle(a, b, c):
        return False
    return a == b or b == c or a == c


def scalene(sides):
    a, b, c = sides
    if not _is_valid_triangle(a, b, c):
        return False
    return a != b and b != c and a != c


def _is_valid_triangle(a, b, c):
    # All sides must be > 0
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Triangle inequality rule
    return (
        a + b >= c and
        b + c >= a and
        a + c >= b
    )