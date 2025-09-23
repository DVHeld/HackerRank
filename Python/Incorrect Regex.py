"""Incorrect Regex

    https://www.hackerrank.com/challenges/incorrect-regex/problem
    """

import re

if __name__ == '__main__':
    test_patterns = [raw_input() for _ in range(int(input()))]
    for pattern in test_patterns:
        try:
            re.compile(pattern)
            print(True)
        except re.error:
            print(False)
