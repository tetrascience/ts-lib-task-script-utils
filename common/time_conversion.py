import dateparser, arrow, datetime
from dateutil import tz


def raw_time_string_to_ts_format(datetime_str, from_zone=None, datetime_formats=[]):
    """ General utility for converting datetimes to Tetrascience standard
    
        Inputs:
            datetime_str - raw datetime
            from_zone - timezone of input can be either string (i.e. "GMT-5") or a timezone type 
                recognized by the arrow.get function such as:
                [dateparser.timezone_parser.StaticTzInfo,dateutil.tz.tz.tzutc,dateutil.tz.tz.tzoffset]
                This will replace the embedded timezone if one is present.
                If neither is present, the input time will not be shifted, and no 'Z' will be
                added to the output.
            datetime - list of arrow format strings to try(https://arrow.readthedocs.io/en/stable/#format)
            
        Output:
                Datetime iso formatted string with millisecond precision in GMT indicated by 'Z' if 
                there was an input from_zone or a timezone embedded in the raw string
                (i.e.: "2019-07-17T14:21:00.000Z").
                If there is no timezone input nad none embedded in the input raw string, the time will
                be changed to the same format, not shifted and nothing appended to the end.
                (i.e. "2019-07-17T11:21:00.000")
    """

    if len(datetime_formats) > 0:  # If formats are provided, use arrow
        initial_parse = arrow.get(datetime_str, datetime_formats)
    else:  # Use dateparser without provided format
        initial_parse = dateparser.parse(datetime_str)
    if initial_parse is None:
        raise ValueError(
            f"Could not parse input datetime string {datetime_str} dateparser or arrow using input formats: {datetime_formats}"
        )

    embedded_zone = initial_parse.tzinfo  # Works for both arrow and dateparser

    # Logic to determine source of the timezone to convert from and
    #  prefer the provided timezone over the embedded one
    from_zone_known = True
    parsed_time = initial_parse
    if from_zone is None and embedded_zone is None:
        from_zone_known = False
    elif from_zone is not None:
        if isinstance(from_zone, str):
            zone_use = tz.gettz(from_zone)
        else:
            zone_use = from_zone

        if embedded_zone is not None:  # use input from_zone
            time_without_zone = str(
                datetime.datetime(  # there may be a cleaner way to do this
                    initial_parse.year,
                    initial_parse.month,
                    initial_parse.day,
                    initial_parse.hour,
                    initial_parse.minute,
                    initial_parse.second,
                    initial_parse.microsecond,
                )
            )
            parsed_time = arrow.get(time_without_zone, tzinfo=zone_use)

    else:  # embedded only if from_zone is not input
        zone_use = embedded_zone

    if from_zone_known:
        datetime_iso_local = arrow.get(str(parsed_time), tzinfo=zone_use)
        iso_indicator_str = "Z"
    else:  # Set to GMT to match output zone and have no shift
        datetime_iso_local = arrow.get(str(parsed_time), tzinfo=tz.gettz("GMT"))
        iso_indicator_str = ""

    datetime_iso = (
        datetime_iso_local.to("GMT")
        .format("YYYY-MM-DDTHH:mm:ss.SSSZ")
        .replace("+0000", iso_indicator_str)
    )
    return datetime_iso
