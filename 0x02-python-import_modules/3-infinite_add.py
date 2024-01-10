#!/usr/bin/python3
import sys

if __name__ == "__main__":
    result = 0
    for arg in sys.argv[1:]:  # Start from index 1 to skip script name
        try:
            result += int(arg)  # Attempt to convert the argument to an integer
        except ValueError:
            pass  # Ignore non-integer arguments

    print(result)
