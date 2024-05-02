#!/usr/bin/python3
"""This module has a script that reads stdin line by
    line and computes metrics
"""
import signal
import re
import sys
from datetime import datetime


status_codes = {
    "200": 0, "301": 0, "400": 0,
    "401": 0, "403": 0, "404": 0,
    "405": 0, "500": 0
    }

total_file_size = 0


def customPrint():
    """A custom print"""
    print("File size: {}".format(total_file_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{}: {}".format(key, value))


# regex pattern to match user input
pattern = re.compile(r'''(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-
                     # matches the ip address
                     \s\[([\d]{1,4}- # matches the year in datetime
                     \d{2}- # matches the month in datetime
                     \d{2}\s # matches the day in datetime
                     \d{2}: # matches the hour in datetime
                     \d{2}: # matches the minutes in datetime
                     \d{2}. # matches the seconds in datetime
                     \d+)\]\s # matches the miliseconds in datetime
                     "GET\s/projects/260\sHTTP/1.1"\s # matches the route
                     (\d{3})\s # matches the status code
                     ([\d]+)$ # matches the file size
                     ''', re.VERBOSE)

if __name__ == "__main__":
    keep_track = 1
    try:
        while True:
            line = input()
            match = pattern.search(line.strip())
            if match:
                matched_groups = match.groups()
                ips = matched_groups[0].split(".")
                status = matched_groups[2]
                file_size = int(matched_groups[3])
                if (
                    any(
                        int(ip) < 1 or int(ip) > 255 for ip in ips
                        ) or status not in status_codes.keys() or
                        (file_size < 1 or file_size > 1024)):
                    continue
                date = matched_groups[1]
                try:
                    # check if datetime is valid
                    datetime.fromisoformat(date)
                except Exception:
                    continue
                total_file_size += file_size
                status_codes[status] += 1
                keep_track += 1
                if keep_track == 10:
                    customPrint()
                    keep_track = 1
                else:
                    customPrint()
                # catch the keyboardinterrupt signal
            # signal.signal(signal.SIGINT, customPrint)
    except (KeyboardInterrupt, EOFError):
        customPrint()
