from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP, KEY_ENTER
import body


class Robot:
    def __init__(self, width, length, map_config, stdscr=None):
        self.stdscr = stdscr
        self.xposition = 4
        self.yposition = 4
        self.collision = False
        self.box = map_config['box']
        self.hurdles_points = [point for hurdle in map_config['hurdles'] for point in hurdle.get_body_coord()]

        self.width = width
        self.length = length

        self._body = body.Body(self.xposition, self.yposition, width, length)
        self._prev_body = None
        self._head_bounder = None

        self.move_dict = {
            KEY_UP: self.up,
            KEY_DOWN: self.down,
            KEY_LEFT: self.left,
            KEY_RIGHT: self.right
        }

    def check_hurdles(self, x, y):
        body_buffer = body.Body(x, y, self.width, self.length)
        if any(body_point[0] == self.box[0][1] for body_point in body_buffer.get_body_coord()) or any(
                body_point[0] == self.box[1][1] for body_point in body_buffer.get_body_coord()) or any(
                body_point[1] == self.box[1][0] for body_point in body_buffer.get_body_coord()) or any(
                body_point[1] == self.box[0][0] for body_point in body_buffer.get_body_coord()):
            return True

        if any(body_point in self.hurdles_points for body_point in body_buffer.get_body_coord()):
            self._prev_body = self._body
            return True
        else:
            self._prev_body = self._body
            self._body = body_buffer
            return False

    def right(self):

        self.collision = self.check_hurdles(self.xposition + 1, self.yposition)
        self._head_bounder = self._body._right_bounder
        self._head_bounder += [self._body._top_bounder[-1], self._body._bottom_bounder[-1]]
        if not self.collision:
            self.xposition += 1

    def left(self):

        self.collision = self.check_hurdles(self.xposition - 1, self.yposition)
        self._head_bounder = self._body._left_bounder
        self._head_bounder += [self._body._top_bounder[0], self._body._bottom_bounder[0]]
        if not self.collision:
            self.xposition -= 1

    def up(self):

        self.collision = self.check_hurdles(self.xposition, self.yposition - 1)
        self._head_bounder = self._body._top_bounder
        if not self.collision:
            self.yposition -= 1

    def down(self):

        self.collision = self.check_hurdles(self.xposition, self.yposition + 1)
        self._head_bounder = self._body._bottom_bounder
        if not self.collision:
            self.yposition += 1

    def make_move(self, command):
        self.move_dict[command]()

    def get_coodrd(self):
        return self.xposition, self.yposition

    def render(self):

        if self._prev_body:
            self._prev_body.render(self.stdscr, ' ')
        self._body.render(self.stdscr, '@')
        if self.collision:
            for point in self._head_bounder:
                self.stdscr.addstr(point[1], point[0], '^')
        self.stdscr.refresh()

import time
def launch_robot_controller(map_config, stdscr=None):
    robot = Robot(2, 2, map_config, stdscr)
    stdscr.addstr(0, 0, str(robot.get_coodrd()))

    while True:
        stdscr.addstr(0, 0, str(robot.get_coodrd()))

        robot.render()

        event = stdscr.getch()



        if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            stdscr.addstr(0, 10, str(event))
            robot.move_dict[event]()
        else:

            stdscr.addstr(0, 10, 'EXITTT in 3 second')
            stdscr.refresh()
            time.sleep(3)
            break

