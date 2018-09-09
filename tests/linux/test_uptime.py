import datetime as dt
from linux_rest_api.system.uptime import parse_uptime, iso8601now


def test_parse_uptime():
    assert parse_uptime("0 0\n") == (0, "P0S")
    assert parse_uptime("17831 1598.40\n") == (17831, "PT4H57M11S")
    assert parse_uptime("104231.54 361598.40\n") == (104231, "P1DT4H57M11S")


def test_iso8601now_three_format(monkeypatch):
    class MockDatetime(dt.datetime):
        @classmethod
        def utcnow(cls):
            return cls(2018, 9, 9, 18, 11, 56, 123456)

    monkeypatch.setattr("datetime.datetime", MockDatetime)
    assert iso8601now() == "2018-09-09T18:11:56.123Z"
