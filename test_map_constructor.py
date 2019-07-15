import pytest
import map_constructor
import robot

from random import randint


@pytest.mark.parametrize('max_x, max_y, max_size, num_hurdles', [
    (0.5, 0.5, 0.5, 0.5)
])
def test_hurdle_fabric_init_values(max_x, max_y, max_size, num_hurdles):
    with pytest.raises(TypeError):
        map_constructor.hurdle_fabric(max_x, max_y, max_size, num_hurdles)


@pytest.mark.parametrize(
    'map_width, map_length, hurdles_max_size, hurdles_count, area', [
        (0.5, 0.5, 0.5, 0.5, 0.5),
        (-10, -20, -30, -40, -50)
    ])
def test_MapConstructor_init_values(map_width, map_length, hurdles_max_size,
                                    hurdles_count, area):
    with pytest.raises(TypeError):
        map_constructor.MapConstructor(map_width, map_length, hurdles_max_size,
                                       hurdles_count, area)


@pytest.mark.parametrize(
    'map_width, map_length, hurdles_max_size, hurdles_count, area', [
        (5, 5, 5, 5, 5)
    ])
def test_MapConstructor_init_area(map_width, map_length, hurdles_max_size,
                                  hurdles_count, area):
    with pytest.raises(TypeError):
        map_constructor.MapConstructor(map_width, map_length, hurdles_max_size,
                                       hurdles_count, area)


range_param = [randint(1, 999) for i in range(4)]


@pytest.mark.parametrize('x, y, width, length', [
    range_param
])
def test_get_hurdlers_points(x, y, width, length):
    robot_obj = robot.Robot(x, y, width, length)
    area = robot_obj.get_initial_area()
    map_obj = map_constructor.MapConstructor(1000, 1000, randint(2, 10), 1000,
                                             area)
    points = map_obj.get_hurdlers_points(area)
    for point in points:
        assert (area['x_left'] < point[0] < area['x_right'])
        assert (area['y_bottom'] < point[1] < area['y_top'])
