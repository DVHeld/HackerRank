"""String Validators

    https://www.hackerrank.com/challenges/string-validators/problem

    String validation module with production-grade validation, error handling and functionality.

    This module provides robust string validation functionality with comprehensive input validation.

    Classes:
        StringCheckingError: Base exception for string checking errors.
        StringValidationError: Raised when input validation fails.
        StringProperties: Results of string character type check.

    Functions:
        validate_input: Validates the input for string validation.
        has_character_types: Checks if the string contains alphanumeric, alphabetic, digit,
        lowercase and uppercase characters.
    """

import logging
from typing import NamedTuple

logger = logging.getLogger(__name__)

if not logger.handlers:
    logger.addHandler(logging.NullHandler())

__all__ = [
    'StringCheckingError',
    'StringValidationError',
    'StringProperties',
    'validate_input',
    'has_character_types'
]

class StringCheckingError(Exception):
    """Base exception for string checking errors."""

class StringValidationError(StringCheckingError):
    """Raised when input validation fails."""

class StringProperties(NamedTuple):
    """Results of string character type check.
    
    Attributes:
        has_alnum: True if string contains alphanumeric characters.
        has_alpha: True if string contains alphabetic characters.
        has_digit: True if string contains digit characters.
        has_lower: True if string contains lowercase characters.
        has_upper: True if string contains uppercase characters.
    """

    has_alnum: bool
    has_alpha: bool
    has_digit: bool
    has_lower: bool
    has_upper: bool

def validate_input(string: str, max_len: int = 1000, /) -> None:
    """Validates the input for string validation.

    Args:
        string (str): The input string to validate.
        max_len (int, optional): The maximum length for the input string. Defaults to 1000.

    Raises:
        TypeError: If input is not of type str.
        TypeError: If max_len is not of type int.
        ValueError: If max_len is not greater than 0.
        StringValidationError: If string is empty.
        StringValidationError: If string length exceeds or equals max_len.
    """

    logger.debug("Beginning input validation.")

    # Type validation
    if not isinstance(string, str):
        raise TypeError(f"Expected input of type str, got {type(string).__name__}.")

    if not isinstance(max_len, int):
        raise TypeError(f"Expected max_len of type int, got {type(max_len).__name__}.")

    # max_len validation
    if max_len < 1:
        raise ValueError(f"max_len must be positive, got {max_len}.")

    # String length validation
    str_len = len(string)
    if not str_len:
        raise StringValidationError("string cannot be empty.")
    if str_len >= max_len:
        raise StringValidationError(
            f"string length ({str_len}) must be less than {max_len}. "
            "Consider increasing max_len."
            )

    logger.debug("Input validated successfully.")

def has_character_types(
    string: str,
    max_len: int = 1000,
    validate: bool = True,
    /) -> StringProperties:
    """Checks if the string contains alphanumeric, alphabetic, digit, lowercase and uppercase
    characters.

    This function sequentially scans the string checking if each character is one of the
    following: alphanumeric, alphabetic, digit, lowercase, uppercase. It then returns a
    StringProperties object containing a boolean value for each of those respective criteria.

    Args:
        string (str): The input string to validate.
        max_len (int, optional): The maximum length for the input string. Defaults to 1000.
        validate (bool, optional): Whether to validate inputs. Defaults to True.

    Raises:
        TypeError: If validate is not of bool type.
        TypeError: If input is not of type str.
        TypeError: If max_len is not of type int.
        ValueError: If max_len is not greater than 0.
        StringValidationError: If string is empty.
        StringValidationError: If string length exceeds or equals max_len.

    Returns:
        StringProperties: Named tuple with boolean flags for each character type.
            - has_alnum: True if string contains alphanumeric characters.
            - has_alpha: True if string contains alphabetic characters.
            - has_digit: True if string contains digit characters.
            - has_lower: True if string contains lowercase characters.
            - has_upper: True if string contains uppercase characters.
    
    Notes:
        - Time complexity: O(k) where k = len(string).
        - Space complexity: O(1).
    
    Examples:
        >>> result = has_character_types('qA2')
        >>> result
        StringProperties(has_alnum=True, has_alpha=True, has_digit=True, has_lower=True, has_upper=True)
        >>> result.has_digit
        True
        >>> result.has_upper
        True
        >>> result = has_character_types('!!!')
        >>> result.has_alnum
        False
    """

    # Validate validate type
    if not isinstance(validate, bool):
        raise TypeError(f"Expected validate to be of bool type, got: {type(validate).__name__}.")

    if validate:
        validate_input(string, max_len)

    logger.debug(
        "Starting validation of string of length %s: %s",
        len(string),
        string[:50] + ('...' if len(string) > 50 else '')
    )

    has_alnum: bool = False
    has_alpha: bool = False
    has_digit: bool = False
    has_lower: bool = False
    has_upper: bool = False

    for char in string:
        if not has_alnum and char.isalnum():
            has_alnum = True
        if not has_alpha and char.isalpha():
            has_alpha = True
        if not has_digit and char.isdigit():
            has_digit = True
        if not has_lower and char.islower():
            has_lower = True
        if not has_upper and char.isupper():
            has_upper = True
        if has_alnum and has_alpha and has_digit and has_lower and has_upper:
            break

    logger.debug(
        "Finished string validation. Results:\n"
        "Contains alnum: %s\n"
        "Contains alpha: %s\n"
        "Contains digit: %s\n"
        "Contains lower: %s\n"
        "Contains upper: %s",
        has_alnum,
        has_alpha,
        has_digit,
        has_lower,
        has_upper
    )
    return StringProperties(
        has_alnum=has_alnum,
        has_alpha=has_alpha,
        has_digit=has_digit,
        has_lower=has_lower,
        has_upper=has_upper
    )

if __name__ == '__main__':
    s = input()

    for result in has_character_types(s):
        print(result)
