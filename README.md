# linux-rest-api - A REST API for Linux!

It makes it possible to configure your entire system (well, parts which are implemented) 
via a REST API. The main advantage is that you don't have to parse all kind of 
configuration files, it is a community effort, all kind of parsers are implemented.

It's the modern version of [Webmin](http://www.webmin.com/).

Examples:

- Add a `pg_hba.conf` entry and reload PostgreSQL configuration.
- Enable/disable a website for nginx and reload.
- Get system state like uptime, free memory or disk space. (Make it easier to monitor.)
- Upgrade your system in an automated way (e.g. apt-get upgrade)
- Stop/start systemd services
- Get status about services
- You can use it as a building block for your appliance.


## Features

- Upload a file anywhere on the filesystem
- Download any file from the system
- Get information about the System (os-release, uptime, kernel version, etc.)


## Security

The process should be run as root, and it should not be exposed to the internet directly,
because it would open a huge security risk on your box.
It's best to use on a closed, trusted internal network, and it still should be protected
by strong authentication over HTTPS. (e.g. with client certificates AND token)

## Requirements

- Any kind of Linux system
- Python 3.6+
- gcc (for installing psutil) or the psutil package pre-installed
