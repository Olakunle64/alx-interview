#!/usr/bin/python3
"""This module has a script that reads stdin line by line and computes metrics"""
import signal
import re
import sys


def customPrint(status_code=None, file_size=0):
    """A custom print"""
    print("File size: {}".format(file_size))
    for key, value in status_code.items():
        print("{}: {}".format(key, value))


def customPrintHandler(signal, frame, status_code, file_size):
    """custom print handler for KeyboardInterrupt"""
    print("File size: {}".format(file_size))
    for key, value in status_code.items():
        print("{}: {}".format(key, value))

def customPrintHandlerWrapper(signal, frame, status_code, file_size):
    """A custom print handler wrapper"""
    customPrintHandler(signal, frame, status_code, file_size)

status_code = {"200": 0, "301": 0, "400": 0,
               "401": 0, "403": 0, "404": 0,
               "405": 0, "500": 0
               }
file_size = 0
keep_track = 0
pattern = re.compile(r'''([0-2]?[0-9]?[0-9]\.){3}([0-2]?[0-9]?[0-9])\s- # matches the ip address
                     \s\[[\d]{1,4}- # matches the year in datetime
                     ([0-1]\d)- # matches the month in datetime
                     ([0-3]?\d)\s # matches the day in datetime
                     ([0-2][\d]): # matches the hour in datetime
                     ([0-6][\d]): # matches the minutes in datetime
                     ([0-6][\d]). # matches the seconds in datetime
                     \d+\]\s # matches the miliseconds in datetime
                     "GET\s/projects/260\sHTTP/1.1"\s # matches the route
                     ([2-5]0[0-5])\s # matches the status code
                     ([\d]+) # matches the file size
                     ''', re.VERBOSE)
for line in sys.stdin:
    if keep_track == 10:
        customPrint(status_code=status_code, file_size=file_size)
        keep_track = 0
    match = pattern.search(line.strip())
    if match:
        matched_groups = match.groups()
        file_size += int(matched_groups[-1].strip())
        if matched_groups[-2].strip() in status_code.keys():
            status_code[matched_groups[-2].strip()] += 1
    signal.signal(
        signal.SIGINT, lambda signal, frame: customPrintHandlerWrapper(
            signal, frame, status_code, file_size
            )
            )
    keep_track += 1
