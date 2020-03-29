from math import pi, e
import os, sys, pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from is_number import isnumber


def test_is_number(snapshot):
    # True cases
    snapshot.assert_match(isnumber(0))
    snapshot.assert_match(isnumber(0.0))
    snapshot.assert_match(isnumber(1))
    snapshot.assert_match(isnumber(1.0))
    snapshot.assert_match(isnumber(1.1))
    snapshot.assert_match(isnumber(-1))
    snapshot.assert_match(isnumber(-1.0))
    snapshot.assert_match(isnumber(-1.1))
    snapshot.assert_match(isnumber("0"))
    snapshot.assert_match(isnumber("0.0"))
    snapshot.assert_match(isnumber("1"))
    snapshot.assert_match(isnumber("1.1"))
    snapshot.assert_match(isnumber(pi))
    snapshot.assert_match(isnumber(e))

    # False cases
    snapshot.assert_match(isnumber("one"))
    snapshot.assert_match(isnumber("pi"))
    snapshot.assert_match(isnumber(True))
    snapshot.assert_match(isnumber(False))
    snapshot.assert_match(isnumber([]))
    snapshot.assert_match(isnumber({}))
