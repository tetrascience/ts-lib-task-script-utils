import common


def test_lunatic_utils():
    assert common.convert_to_float("-") == None
    assert common.convert_to_float("20") == 20
