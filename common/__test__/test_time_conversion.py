import pytest, sys
from dateutil import tz
from time_conversion import raw_time_string_to_ts_format


def test_no_timezone():
    raw_expect = [
        ("2019-07-17 11:21:00", "2019-07-17T11:21:00.000"),
        ("2020-06-18 13:17:57.54036", "2020-06-18T13:17:57.540"),
    ]
    for raw, expect in raw_expect:
        assert raw_time_string_to_ts_format(raw) == expect


def test_embedded_timezone():
    raw_expect = [
        ("2020-03-06T17:19:45.706000-05:00", "2020-03-06T22:19:45.706Z"),
        ("2020-04-30T20:27:41.000Z", "2020-04-30T20:27:41.000Z"),
    ]
    for raw, expect in raw_expect:
        assert raw_time_string_to_ts_format(raw) == expect


def test_input_timezone():
    raw_timezone_expect = [
        ("2019-07-17 11:21:00", "GMT-5", "2019-07-17T16:21:00.000Z"),
        (
            "2019-07-17 11:21:00",
            tz.tzoffset("GMT", -5 * 60 * 60),
            "2019-07-17T16:21:00.000Z",
        ),
        ("2019-07-17 11:21:00", tz.tzutc(), "2019-07-17T11:21:00.000Z"),
        ("2020-04-30T20:27:41.000Z", "GMT+3", "2020-04-30T17:27:41.000Z"),
    ]
    for raw, timezone, expect in raw_timezone_expect:
        assert raw_time_string_to_ts_format(raw, from_zone=timezone) == expect


def test_input_timezone_overrides_embedded():
    raw_timezone_expect = [
        ("2020-03-06T17:19:45.706000-05:00", "GMT+5", "2020-03-06T12:19:45.706Z")
    ]
    for raw, timezone, expect in raw_timezone_expect:
        assert raw_time_string_to_ts_format(raw, from_zone=timezone) == expect


def test_unreadable_format():
    try:
        raw_time_string_to_ts_format("20200512T235847.070Z")
    except:
        exc_info = sys.exc_info()
        assert exc_info[
            0
        ] == ValueError and "Could not parse input datetime string" in str(exc_info[1])


def test_format_strings():
    raw_format_expect = [
        (
            "2020-03-06T17:19:45.706000-05:00",
            ["YYYY-MM-DDTHH:mm:ss.SZZ"],
            "2020-06-03T22:19:45.706Z",
        ),
        ("20200512T235847.070Z", ["YYYYMMDDTHHmmss.SZ"], "2020-05-12T23:58:47.070Z"),
    ]


def test_YDM_order():
    raw_format_expect = [
        (
            "2020-03-06T17:19:45.706000-05:00",
            ["YYYY-DD-MMTHH:mm:ss.SZZ"],
            "2020-06-03T22:19:45.706Z",
        )
    ]
    for raw, formats, expect in raw_format_expect:
        assert raw_time_string_to_ts_format(raw, datetime_formats=formats) == expect


def test_bad_timezone():
    try:
        raw_time_string_to_ts_format(
            "2020-03-06T17:19:45.706000-05:00", from_zone="GMT+500"
        )
    except:
        exc_info = sys.exc_info()
        assert exc_info[0] == TypeError

