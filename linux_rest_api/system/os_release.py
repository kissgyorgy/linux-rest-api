"""
Parse Linux distro information from /etc/os-release file.
Details about the os-release file:
https://www.freedesktop.org/software/systemd/man/os-release.html

The announcement about it by Poettering:
http://0pointer.de/blog/projects/os-release
"""
from marshmallow import Schema, fields
from pathlib import Path


class OSRelease(Schema):
    name = fields.Str(default="Linux")
    version = fields.Str(default=None)
    id = fields.Str(default="linux")
    id_like = fields.Str(default=None)
    version_codename = fields.Str(default=None)
    version_id = fields.Str(default=None)
    pretty_name = fields.Str(default=None)
    ansi_color = fields.Str(default=None)
    cpe_name = fields.Str(default=None)

    home_url = fields.Url(default=None)
    support_url = fields.Url(default=None)
    bug_report_url = fields.Url(default=None)
    privacy_policy_url = fields.Url(default=None)

    build_id = fields.Str(default=None)
    variant = fields.Str(default=None)
    variant_id = fields.Str(default=None)


def parse_os_release(os_release: str):
    schema = OSRelease()

    release_data = dict()

    for line in os_release.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, value = line.split("=")
        key = key.lower()
        release_data[key] = value.strip('"')

    return schema.dump(release_data)


def get_os_release():
    os_release = Path("/etc/os-release").read_text()
    return parse_os_release(os_release)
