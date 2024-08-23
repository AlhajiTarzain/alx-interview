#!/usr/bin/python3
"""
Defines a UTF-8 Validation function
"""

def validUTF8(data):
    """
    UTF-8 Validation
    Args:
        data (list[int]): an array of characters represented as 1-byte integers
    Returns:
        (True): if all characters in data are valid UTF-8 code points
        (False): if one or more characters in data are invalid code points
    """
    # Masks to check specific bits
    first_bit_mask = 1 << 7    # 10000000 in binary
    second_bit_mask = 1 << 6   # 01000000 in binary
    
    # Tracks the number of continuation bytes expected
    remaining_bytes = 0

    for byte in data:
        most_significant_bit_mask = 1 << 7  # Start with the leftmost bit

        if remaining_bytes == 0:
            # Count the number of leading 1's in the first byte
            while most_significant_bit_mask & byte:
                remaining_bytes += 1
                most_significant_bit_mask = most_significant_bit_mask >> 1
            
            if remaining_bytes == 0:
                continue  # 1-byte character

            if remaining_bytes == 1 or remaining_bytes > 4:
                return False  # Invalid UTF-8 character

        else:
            # Check if the byte is a valid continuation byte (starts with '10')
            if not (byte & first_bit_mask and not (byte & second_bit_mask)):
                return False

        remaining_bytes -= 1

    # Return True if all bytes are valid and there are no remaining continuation bytes expected
    return remaining_bytes == 0
