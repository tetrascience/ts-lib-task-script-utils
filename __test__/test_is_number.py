from common.is_number import isnumber
import common


def test_is_number():
    assert isnumber(10)
    assert isnumber("10")
    assert isnumber("NaN")

    assert not common.isnumber(True)
    assert not isnumber("cheese")
