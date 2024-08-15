#!/usr/bin/python3
"""
A script: Reads standard input line by line and computes metrics
"""

def parseLogs():
    """
    Reads logs from standard input and generates reports.
    Reports:
        * Prints log size after reading every 10 lines & at KeyboardInterrupt.
    Raises:
        KeyboardInterrupt: Handles this exception to print the report.
    """
    stdin = __import__('sys').stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            
            try:
                # Extract file size and status code from the line
                fileSize += int(line[-1])
                if line[-2] in codes:
                    statusCodes[line[-2]] = statusCodes.get(line[-2], 0) + 1
            except (IndexError, ValueError):
                # Skip lines that don't match the expected format
                pass
            
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
        
        # Final report after all lines are processed
        report(fileSize, statusCodes)
    
    except KeyboardInterrupt:
        # Print the report on a KeyboardInterrupt (e.g., CTRL + C)
        report(fileSize, statusCodes)
        raise


def report(fileSize, statusCodes):
    """
    Prints generated report to standard output.
    Args:
        fileSize (int): Total log size after every 10 successfully read lines.
        statusCodes (dict): Dictionary of status codes and their counts.
    """
    print("File size: {}".format(fileSize))
    for key in sorted(statusCodes.keys()):
        print("{}: {}".format(key, statusCodes[key]))


if __name__ == '__main__':
    parseLogs()
