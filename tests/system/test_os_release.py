from pathlib import Path
import pytest
from linux_rest_api.system.os_release import OSRelease, parse_os_release


def test_parse_xenial(datadir):
    xenial_os_release = (datadir / "os-release-ubuntu-xenial").read_text()
    result = parse_os_release(xenial_os_release)
    assert result == {
        "name": "Ubuntu",
        "version": "16.04.4 LTS (Xenial Xerus)",
        "id": "ubuntu",
        "id_like": "debian",
        "version_codename": "xenial",
        "version_id": "16.04",
        "pretty_name": "Ubuntu 16.04.4 LTS",
        "ansi_color": None,
        "cpe_name": None,
        "home_url": "http://www.ubuntu.com/",
        "support_url": "http://help.ubuntu.com/",
        "bug_report_url": "http://bugs.launchpad.net/ubuntu/",
        "privacy_policy_url": None,
        "build_id": None,
        "variant": None,
        "variant_id": None,
    }


def test_parse_bionic(datadir):
    bionic_os_release = (datadir / "os-release-ubuntu-bionic").read_text()
    result = parse_os_release(bionic_os_release)
    assert result == {
        "name": "Ubuntu",
        "version": "18.04.1 LTS (Bionic Beaver)",
        "id": "ubuntu",
        "id_like": "debian",
        "version_codename": "bionic",
        "version_id": "18.04",
        "pretty_name": "Ubuntu 18.04.1 LTS",
        "ansi_color": None,
        "cpe_name": None,
        "home_url": "https://www.ubuntu.com/",
        "support_url": "https://help.ubuntu.com/",
        "bug_report_url": "https://bugs.launchpad.net/ubuntu/",
        "privacy_policy_url": "https://www.ubuntu.com/legal/terms-and-policies/privacy-policy",
        "build_id": None,
        "variant": None,
        "variant_id": None,
    }


def test_blank_lines_should_be_ignored(datadir):
    os_release = (datadir / "os-release-blank-lines").read_text()
    result = parse_os_release(os_release)
    assert result == {
        "name": "Ubuntu",
        "version": "16.04.4 LTS (Xenial Xerus)",
        "id": "linux",
        "id_like": None,
        "version_codename": None,
        "version_id": None,
        "pretty_name": "Ubuntu 16.04.4 LTS",
        "ansi_color": None,
        "cpe_name": None,
        "home_url": None,
        "support_url": None,
        "bug_report_url": None,
        "privacy_policy_url": None,
        "build_id": None,
        "variant": None,
        "variant_id": None,
    }


def test_defaults(datadir):
    result = parse_os_release("")
    assert result["name"] == "Linux"
    assert result["id"] == "linux"


def test_comments_should_be_ignored(datadir):
    os_release = (datadir / "os-release-comments").read_text()
    result = parse_os_release(os_release)
    assert result == {
        "name": "Ubuntu",
        "version": "16.04.4 LTS (Xenial Xerus)",
        "id": "ubuntu",
        "id_like": None,
        "version_codename": None,
        "version_id": "16.04",
        "pretty_name": "Ubuntu 16.04.4 LTS",
        "ansi_color": None,
        "cpe_name": None,
        "home_url": None,
        "support_url": None,
        "bug_report_url": None,
        "privacy_policy_url": None,
        "build_id": None,
        "variant": None,
        "variant_id": None,
    }
