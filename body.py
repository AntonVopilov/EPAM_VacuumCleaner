class Body:
    def __init__(self, x: int, y: int, width: int, length: int):
        self.x_left_top = x
        self.y_left_top = y
        self.width = width  # associated with x direction
        self.length = length  # associated with y direction
        self._body_points = []
        self._top_bounder = []
        self._bottom_bounder = []
        self._right_bounder = []
        self._left_bounder = []

    def body_coord(self):
        self.set_to_empty()
        for i in range(self.width):
            self._top_bounder.append([self.x_left_top + i, self.y_left_top])
            self._bottom_bounder.append([self.x_left_top + i, self.y_left_top + self.length])
        for i in range(1, self.length):
            self._right_bounder.append([self.x_left_top + self.width - 1, self.y_left_top + i])
            self._left_bounder.append([self.x_left_top, self.y_left_top + i])

    def get_body_coord(self):
        self.body_coord()
        self._body_points += self._top_bounder + self._bottom_bounder
        self._body_points += self._left_bounder + self._right_bounder
        return self._body_points

    def set_to_empty(self):
        self._body_points = []
        self._top_bounder = []
        self._bottom_bounder = []
        self._right_bounder = []
        self._left_bounder = []

    def render(self, stdscr, char):
        self.get_body_coord()
        for point in self._body_points:
            stdscr.addstr(point[1], point[0], char)
        stdscr.refresh()
