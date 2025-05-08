#!/usr/bin/python3
from sys import stdin
import re
from collections import defaultdict


size = 0
status = defaultdict(int)
lines = 0
codes = ['200', '301', '400', '401', '403', '404', '405', '500']
log = re.compile(r'^\d{1,3}(\.\d{1,3}){3} - \[.*?\] "GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$')


def stats_print():
    print("File size: {}".format(size))
    for code in sorted(codes):
        if status[code]:
            print("{}: {}".format(code, status[code]))


try:
    for line in stdin:
        match = log.match(line.strip())
        if match:
            statusg, sizeg = match.group(2), match.group(3)
            size += int(sizeg)
            if statusg in codes:
                status[statusg] += 1
        lines += 1
        if lines == 10:
            stats_print()
            lines = 0
except KeyboardInterrupt:
    stats_print()
    raise
stats_print()
