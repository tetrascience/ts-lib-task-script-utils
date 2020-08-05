import dateparser, arrow, datetime
from dateutil import tz


def raw_time_string_to_ts_format(datetime_str, from_zone=None, datetime_formats=[]):
    """ General utility for converting datetimes to Tetrascience standard
    
        Inputs:
            datetime_str - raw datetime
            from_zone - timezone of input can be either string (i.e. GMT-5) or one of these types:
                [dateparser.timezone_parser.StaticTzInfo,dateutil.tz.tz.tzutc,dateutil.tz.tz.tzoffset]
                This will be preferred to the embedded timezone if one is present.
                If neither is present, the input zone will be assumed GMT and no 'Z' will be
                added to the output.
            datetime - list of arrow format strings to try(https://arrow.readthedocs.io/en/stable/#format)
            
        Outpu:
                datetime iso formatted string with millisecond precision in GMT indicated by 'Z' if 
                there was an input from_zone or a timezone embedded in the raw string
                    i.e.: "20200512T235847.070Z"
    """
    timezone_types = [
        dateparser.timezone_parser.StaticTzInfo,
        tz.tz.tzutc,
        tz.tz.tzoffset,
    ]

    if len(datetime_formats) > 0:  # If formats are provided, use arrow
        initial_parse = arrow.get(datetime_str, datetime_formats)
    else:  # Use dateparser without provided format
        initial_parse = dateparser.parse(datetime_str)
    if initial_parse is None:
        raise ValueError(
            f"Could not parse input datetime string {datetime_str} dateparser or arrow using input formats: {datetime_formats}"
        )

    embedded_zone = initial_parse.tzinfo  # Works for both arrow and dateparser

    # prefer the provided timezone to the embedded one
    from_zone_known = True
    parsed_time = initial_parse
    if from_zone is None and embedded_zone is None:
        from_zone_known = False
    elif from_zone is not None:  # use input from_zone
        rep_time = str(
            datetime.datetime(
                initial_parse.year,
                initial_parse.month,
                initial_parse.day,
                initial_parse.hour,
                initial_parse.minute,
                initial_parse.second,
                initial_parse.microsecond,
            )
        )  # there may be a cleaner way to do this
        parsed_time = arrow.get(rep_time, tzinfo=tz.gettz(from_zone))
    elif from_zone is None:  # embedded only if none is input
        from_zone = embedded_zone

    # Make sure we have a valid timezone to use
    if any(
        [isinstance(from_zone, typ) for typ in timezone_types]
    ):  # This may be input or embedded
        zone_use = from_zone
    else:  # this will handle input strings
        zone_use = tz.gettz(from_zone)

    if from_zone_known:
        datetime_iso_local = arrow.get(str(parsed_time), tzinfo=zone_use)
        iso_indicator_str = "Z"
    else:  # Default to GMT
        datetime_iso_local = arrow.get(str(parsed_time), tzinfo=tz.gettz("GMT"))
        iso_indicator_str = ""

    datetime_iso = (
        datetime_iso_local.to("GMT")
        .format("YYYY-MM-DDTHH:mm:ss.SSSZ")
        .replace("+0000", iso_indicator_str)
    )
    return datetime_iso
