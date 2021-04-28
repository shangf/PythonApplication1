# Author: Frank Shang
# Date: 04/28/2021
# Description: This program contains a class called Taxicab. It keeps track of the shifts in distance and displays the odometer for each Taxicab object.

class Taxicab:
    """Class that creates Taxicab objects that determines x, y coordinates and the cab's odometer."""

    def __init__(self, x_coord, y_coord):
        """Initalization of private data attributes with arguments x_coord and y_coord. Initalizes odometer to 0 as well."""
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """Method that returns the object's x coordinate. """
        return self._x_coord

    def get_y_coord(self):
        """Method that returns the object's y coordinate."""
        return self._y_coord

    def get_odometer(self):
        """Method that returns the object's odometer."""
        return self._odometer

    def move_x(self, new_x_coord):
        """Method that assigns a new value to x coordinate. Keeps a counter of the shift in distance through absolute value function."""
        self._x_coord += new_x_coord
        self._odometer += abs(new_x_coord)

    def move_y(self, new_y_coord):
        """Method that assigns a new value to y coordinate. Keeps a counter of the shift in distance through absolute value function."""
        self._y_coord += new_y_coord
        self._odometer += abs(new_y_coord)

cab = Taxicab(5, -8)
print(cab.get_x_coord())
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.get_odometer())
print(cab.get_x_coord())
print(cab.get_y_coord())
