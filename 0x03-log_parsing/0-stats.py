#!/usr/bin/python3
"""
Script to parse logs and compute metrics.
"""

import sys

def print_stats(file_size, status_codes):
    """
    Function to print the accumulated metrics.
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    file_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) > 6:
                # Extract the file size and status code
                file_size += int(parts[-1])
                status_code = parts[-2]

                if status_code in status_codes:
                    status_codes[status_code] += 1

            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        # Print metrics on KeyboardInterrupt (CTRL+C)
        print_stats(file_size, status_codes)
        raise

    # Print final stats after all lines are processed
    print_stats(file_size, status_codes)
