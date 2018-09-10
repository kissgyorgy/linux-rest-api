import datetime as dt
from pathlib import Path


def _prepend_if_not_zero(value, unit: str, uptime: str):
    return f"{value}{unit}{uptime}" if value > 0 else uptime


def iso8601_duration(seconds: float):
    """Convert a duration in seconds to ISO8601 duration format.
    See: https://en.wikipedia.org/wiki/ISO_8601#Durations
    """
    minutes, seconds = divmod(seconds, 60)
    seconds = int(seconds) if seconds % 1 == 0 else round(seconds, 2)
    duration = _prepend_if_not_zero(seconds, "S", "")

    hours, minutes = divmod(int(minutes), 60)
    duration = _prepend_if_not_zero(minutes, "M", duration)

    days, hours = divmod(hours, 24)
    duration = _prepend_if_not_zero(hours, "H", duration)

    if duration:
        duration = "T" + duration

    months, days = divmod(days, 30)
    duration = _prepend_if_not_zero(days, "D", duration)

    years, months = divmod(months, 12)
    duration = _prepend_if_not_zero(months, "M", duration)
    duration = _prepend_if_not_zero(years, "Y", duration)

    # 'P' would be an invalid zero value by itself
    duration = "P" + (duration or "0S")

    return duration


def parse_uptime(uptime: str):
    """Parses the output of /proc/uptime."""
    total_seconds, _ = uptime.split()
    # I don't think anybody needs microsecond precision and this is way easier to parse
    total_seconds = float(total_seconds)
    return total_seconds, iso8601_duration(total_seconds)


def get_uptime():
    uptime = Path("/proc/uptime").read_text()
    return parse_uptime(uptime)


def iso8601now():
    isoformat = dt.datetime.utcnow().isoformat()
    # this is more in line with other formats and the ISO8601 standard
    return isoformat[:-3] + "Z"


def get_load():
    loadavg = Path("/proc/loadavg").read_text()
    # The first three numbers are the load averages for 1, 5 and 15 minutes
    return [float(l) for l in loadavg.split()[:3]]
