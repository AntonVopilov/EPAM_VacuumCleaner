import curses
import time
from curses import textpad
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
import hurdles
import robot


def main_graphics(stdscr):
    stdscr.keypad(1)
    curses.noecho()
    curses.curs_set(0)

    stdscr.clear()
    sh, sw = stdscr.getmaxyx()
    box = [[1, 1], [sh - 2, sw - 2]]  # [[ul_y, ul_x], [dr_y, dr_x]]
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    msg1 = 'Vacuum Cleaner Controller'
    stdscr.addstr(sh // 2, sw // 2 - len(msg1)//2, msg1)
    msg2 = 'for EXIT press anything except control commands'
    stdscr.addstr(sh // 2 + 1, sw // 2- len(msg2)//2, msg2)
    stdscr.refresh()
    time.sleep(3)

    stdscr.clear()
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    time.sleep(2)

    hurdles_objts = hurdles.hurdle_fabric(box[1][1] - 1, box[1][0] - 1, 6, 20)
    map_config = {'hurdles': hurdles_objts, 'box': box}
    for hurdle in hurdles_objts:
        hurdle.render(stdscr, '*')
    time.sleep(2)

    robot.launch_robot_controller(map_config, stdscr)


if __name__ == '__main__':
    curses.wrapper(main_graphics)
