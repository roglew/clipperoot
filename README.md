Clipperoot
==========

Overview
--------
This script is a sample attack against password managers which have you copy and paste passwords into websites/applications. It works by constantly checking the clipboard and if it looks like a password, it attempts to use it to get root access on your computer and run a command. It should work on linux and Mac.

Installation
------------
This script has a few dependencies, but they can be installed using pip and the provided requirements.txt file

    pip install -r /path/to/requirements.txt

Usage
-----

    python clipperoot.py -c COMMAND_TO_RUN_ON_ROOT

When the root password is copied, the command will be run as root, and the working password, stdout from the command, and stderr from the command will be printed to stdout.