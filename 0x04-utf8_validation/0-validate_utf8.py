#!/usr/bin/python3
"""
This module contains a function that checks if a given data set
represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Checks if the given data set represents a valid UTF-8 encoding.
    
    :param data: List of integers representing the data bytes.
    :return: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        # Get the last 8 bits of the integer
        byte = num & 0xFF
        
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # The subsequent bytes must start with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
