import pytest
import robot
from random import randint


@pytest.mark.parametrize('x, y, width, length', [
    (0.5, 0.5, 0.5, 0.5)
])
def test_body_init_values(x, y, width, length):
    with pytest.raises(TypeError):
        robot.Robot(x, y, width, length)


range_param = [randint(1, 100) for i in range(4)]


@pytest.mark.parametrize('x, y, width, length', [
    range_param
])
def test_robot_parametrs(x, y, width, length):
    robot_obj = robot.Robot(x, y, width, length)
    assert robot_obj.length == length
    assert robot_obj.length == length
    assert robot_obj.x_position == x
    assert robot_obj.y_position == y
    assert robot_obj.get_coodrd() == (x, y)


range_param = [randint(1, 100) for i in range(4)]


@pytest.mark.parametrize('x, y, width, length', [
    range_param
])
def test_robot_move_methods(x, y, width, length):
    robot_obj = robot.Robot(x, y, width, length)
    robot_obj.right()
    assert robot_obj.get_coodrd() == (x + 1, y)
    robot_obj.up()
    assert robot_obj.get_coodrd() == (x + 1, y - 1)
    robot_obj.left()
    assert robot_obj.get_coodrd() == (x, y - 1)
    robot_obj.down()
    assert robot_obj.get_coodrd() == (x, y)


range_param = [randint(1, 100) for i in range(4)]


@pytest.mark.parametrize('x, y, width, length', [
    range_param
])
def test_robot_rotate_methods(x, y, width, length):
    robot_obj = robot.Robot(x, y, width, length)
    direction_index = robot_obj.direct_indx

    robot_obj.rotate_counterclockwise()
    assert robot_obj.width == length
    assert robot_obj.length == width
    assert direction_index + 1 == robot_obj.direct_indx
    robot_obj.rotate_clockwise()
    assert robot_obj.width == width
    assert robot_obj.length == length
    assert direction_index == robot_obj.direct_indx
