#!/usr/bin/python3
"""UTF-8 Validation"""
from typing import List


def validUTF8(data):
    bytes_remaining = 0

    for byte in data:
        # If no bytes remaining from previous sequence
        if bytes_remaining == 0:
            # Determine the number of bytes in the current sequence
            if byte >> 7 == 0b0:
                bytes_remaining = 0  # Single-byte character
            elif byte >> 5 == 0b110:
                bytes_remaining = 1  # Two-byte character
            elif byte >> 4 == 0b1110:
                bytes_remaining = 2  # Three-byte character
            elif byte >> 3 == 0b11110:
                bytes_remaining = 3  # Four-byte character
            else:
                return False  # Invalid byte

            # Handle overlong encodings and out-of-range byte values
            if (
                bytes_remaining > 0 and byte >> (7 - bytes_remaining)
                != (0b11111111 >> (8 - bytes_remaining))
            ):
                return False
        else:
            # Check if the byte is a continuation byte
            if byte >> 6 != 0b10:
                return False

            bytes_remaining -= 1

    # Ensure that all multi-byte sequences are complete
    return bytes_remaining == 0
