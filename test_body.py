import pytest
import body
from random import randint


@pytest.mark.parametrize('x, y, width, length', [
    (0.5, 0.5, 0.5, 0.5)
])
def test_body_init_values(x, y, width, length):
    with pytest.raises(TypeError):
        body.Body(x, y, width, length)


range_param = [randint(1, 100) for i in range(4)]


@pytest.mark.parametrize('x, y, width, length', [
    range_param
])
def test_body_parametrs(x, y, width, length):
    body_obj = body.Body(x, y, width, length)
    assert body_obj.length == length
    assert body_obj.length == length
    assert body_obj.x_left_top == x
    assert body_obj.y_left_top == y


range_param = [randint(1, 1000) for i in range(4)]


@pytest.mark.parametrize('x, y, width, length', [
    range_param
])
def test_calculate_body_coord(x, y, width, length):
    body_obj = body.Body(x, y, width, length)
    assert len(body_obj._top_bounder) == width
    assert len(body_obj._left_bounder) == length - 1


range_param = [randint(1, 1000) for i in range(4)]


@pytest.mark.parametrize('x, y, width, length', [
    range_param
])
def test_get_body_center(x, y, width, length):
    body_obj = body.Body(x, y, width, length)
    assert len(body_obj.get_body_coord()) == 2 * width + 2 * (length - 1)
