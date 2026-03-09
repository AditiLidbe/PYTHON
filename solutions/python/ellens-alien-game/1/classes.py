class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate."""

    # Class variable to track total aliens created
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        # Instance variables
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

        # Increment class counter whenever a new alien is created
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement Alien health by one point."""
        self.health -= 1

    def is_alive(self):
        """Return True if Alien is alive, False otherwise."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        """Placeholder for future collision detection logic."""
        pass


def new_aliens_collection(positions):
    """Create a list of Alien objects from a list of coordinate tuples."""
    return [Alien(x, y) for x, y in positions]