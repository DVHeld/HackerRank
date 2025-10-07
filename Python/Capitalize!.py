#!/bin/python3
"""Capitalize!

    https://www.hackerrank.com/challenges/capitalize/problem

    Word for word capitalization module with production-grade validation, error handling and
    functionality.

    This module provides functionality to capitalize a string's words and to validate the
    inputs needed for this.

    Classes:
        CapitalizingError: Base exception for capitalization errors.
        CapitalizingValidationError: Raised when input validation fails.

    Functions:
        solve: Capitalizes all the words in the given string.
        validate_input: Validates the user inputs for capitalizing a string.
    """

import math
import os
import random
import re
import sys
import logging

logger = logging.getLogger(__name__)

if not logger.handlers:
    logger.addHandler(logging.NullHandler())

__all__ = [
    'CapitalizingError',
    'CapitalizingValidationError',
    'validate_input',
    'solve'
]

class CapitalizingError(Exception):
    """Base exception for capitalizing errors."""

class CapitalizingValidationError(CapitalizingError):
    """Raised when input validation fails."""

def validate_input(
    string: str,
    max_len: int = 999,
    only_alnum: bool = True,
    /) -> None:
    """Validates the user inputs for capitalizing a string.

    Args:
        string (str): The string to capitalize.
        max_len (int, optional): The string's maximum length. Defaults to 999.
        only_alnum (bool, optional): Whether to allow only alphanumeric characters and spaces.
                                     Defaults to True.

    Raises:
        TypeError: If inputs are of the wrong type.
        CapitalizingValidationError: If string is empty.
        CapitalizingValidationError: If max_len is not a positive integer (max_len > 0).
        CapitalizingValidationError: If string length exceeds max_len.
        CapitalizingValidationError: If only_alnum is True and string contains non-alphanumeric or
                                     non-space characters.
    """

    logger.debug("Beginning input validation.")
    if not isinstance(string, str):
        raise TypeError(
            f"string must be of str type, got {type(string).__name__}."
        )
    if not isinstance(max_len, int):
        raise TypeError(
            f"max_len must be of int type, got {type(max_len).__name__}."
        )
    if not isinstance(only_alnum, bool):
        raise TypeError(
            f"only_alnum must be of bool type, got {type(only_alnum).__name__}."
        )

    str_len: int = len(string)
    if not str_len:
        raise CapitalizingValidationError(
            "string cannot be empty. Please provide at least one character."
        )
    if max_len < 1:
        raise CapitalizingValidationError(
            f"max_len must be a positive integer (max_len > 0), received {max_len}."
        )
    if str_len > max_len:
        raise CapitalizingValidationError(
            f"string length ({str_len}) cannot exceed max_len ({max_len}). "
            "Please provide a shorter string or increase max_len."
        )

    if only_alnum:
        for index, character in enumerate(string):
            if not character.isalnum() and not character == ' ':
                raise CapitalizingValidationError(
                    f"string of length {str_len} contains forbidden non-alphanumeric or space"
                    f" character '{repr(character)}' (Unicode: U+{ord(character):04X}) at position"
                    f" {index}. Only alphanumeric characters and spaces are allowed. Consider "
                    "setting only_alnum to False."
                )
    logger.debug("Finished input validation.")

def solve(
    string: str,
    max_len: int = 999,
    only_alnum: bool = True,
    validate: bool = True,
    /) -> str:
    """Capitalizes all the words in the given string.

    Capitalizes the first alphabetic character after each space or at the start of the string.
    Preserves exact spacing and structure of the input. Non-alphabetic characters (numbers,
    punctuation) are unchanged.

    Args:
        string (str): The string to capitalize.
        max_len (int, optional): The string's maximum length. Defaults to 999.
        only_alnum (bool, optional): Whether to allow only alphanumeric characters and spaces.
                                     Defaults to True.
        validate (bool, optional): Whether to validate inputs. Defaults to True.

    Raises:
        TypeError: If inputs are of the wrong type.
        CapitalizingValidationError: If string is empty.
        CapitalizingValidationError: If max_len is not a positive integer (max_len > 0).
        CapitalizingValidationError: If string length exceeds max_len.
        CapitalizingValidationError: If string contains non-alphanumeric or space characters.

    Returns:
        str: The capitalized string.

    Example usage:
        >>> s = solve('mary ann')
        >>> print(s)
        'Mary Ann'

        >>> s = solve('12abc   nAn')
        >>> print(s)
        '12abc   Nan'

        >>> s = solve('###')
        # Raises error.
        
        >>> solve('  leading spaces')
        '  Leading Spaces'

        >>> solve('trailing  ')
        'Trailing  '
        
        >>> solve('a')
        'A'
        
        >>> solve("mary-jane o'brien", only_alnum=False)
        'Mary-Jane O'Brien'

    Notes:
        - Time complexity: O(n), where n is len(string).
        - Space complexity: O(n), where n is len(string).
    """

    if not isinstance(validate, bool):
        raise TypeError(
            f"validate must be of bool type, got {type(validate).__name__}."
        )

    if validate:
        validate_input(string, max_len, only_alnum)

    logger.debug("Started capitalization of string %s of length %s.",
        repr(string[:50]) + ('...' if len(string) > 50 else ''),
        len(string)
    )

    capitalized: list[str] = []
    # Capitalize if letter after space, lowercase the rest, preserve spacing and structure.
    for index, character in enumerate(string):
        if index == 0 or string[index - 1] == ' ':
            capitalized.append(character.upper() if character.isalpha() else character)
        else:
            capitalized.append(character.lower() if character.isalpha() else character)
    return ''.join(capitalized)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s: str = input()

    result: str = solve(s)

    fptr.write(result + '\n')

    fptr.close()
