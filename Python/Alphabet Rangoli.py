"""Alphabet Rangoli

    https://www.hackerrank.com/challenges/alphabet-rangoli/problem

    Alphabet Rangoli creation module with production-grade validation, error handling and
    functionality.

    This module provides functionality to build or print Alphabet Rangoli patterns of differing
    sizes and to validate the inputs needed for this.

    Classes:
        AlphabetRangoliError: Base exception for Alphabet Rangoli building errors.
        AlphabetRangoliValidationError: Raised when input validation fails.

    Functions:
        build_rangoli: Builds an Alphabet Rangoli of the given size.
        print_rangoli: Prints an Alphabet Rangoli of the given size.
        validate_inputs: Validates the user inputs for building an Alphabet Rangoli.
    """

import logging

logger = logging.getLogger(__name__)

if not logger.handlers:
    logger.addHandler(logging.NullHandler())

__all__ = [
    'AlphabetRangoliError',
    'AlphabetRangoliValidationError',
    'build_rangoli',
    'print_rangoli',
    'validate_inputs'
]

class AlphabetRangoliError(Exception):
    """Base exception for string checking errors."""

class AlphabetRangoliValidationError(AlphabetRangoliError):
    """Raised when input validation fails."""

def build_rangoli(
    size: int,
    fill: str = '-',
    pattern: str = 'abcdefghijklmnopqrstuvwxyz',
    max_size: int = 26,
    validate: bool = True,
    /) -> str:
    """Builds an Alphabet Rangoli of the given size.

    Args:
        size (int): The size (amount of different letters) of the Rangoli.
        fill (str, optional): The fill to use. Must be a single character. Defaults to '-'.
        pattern (str, optional): The base characters to build the pattern with.  Cannot be empty.
                                 Defaults to the lowercase english alphabet
                                 'abcdefghijklmnopqrstuvwxyz'.
        max_size (int, optional): The maximum number of different letters. Defaults to 26.
        validate (bool, optional): Whether to validate inputs. Defaults to True.

    Raises:
        TypeError: If inputs are of the wrong type.
        AlphabetRangoliValidationError: If size is not positive (size > 0).
        AlphabetRangoliValidationError: If max_size is not positive (max_size > 0).
        AlphabetRangoliValidationError: If size exceeds max_size.
        AlphabetRangoliValidationError: If fill or pattern are empty.

    Returns:
        str: The built rangoli string.

    Examples:
        >>> rangoli = build_rangoli(3)
        >>> print(rangoli)
        ----c----
        --c-b-c--
        c-b-a-b-c
        --c-b-c--
        ----c----

        >>> rangoli = build_rangoli(1)
        >>> print(rangoli)
        a

        >>> rangoli = build_rangoli(3, fill='.', pattern='012')
        >>> print(rangoli)
        ....2....
        ..2.1.2..
        2.1.0.1.2
        ..2.1.2..
        ....2....

    Notes:
        - Total lines: 2 * size - 1.
        - Line width: 4 * size - 3.
        - Pattern is vertically and horizontally symmetric.
        - If size > len(pattern), the pattern is repeated as needed.
        - Time complexity O(size^2).
        - Space complexity O(size^2).
    """

    if not isinstance(validate, bool):
        raise TypeError(f"validate must be of bool type, got {type(validate).__name__}.")

    if validate:
        validate_inputs(size, fill, pattern, max_size)

    logger.debug("Starting rangoli construction of size %s.", size)

    # Build the base pattern
    pattern_len: int = len(pattern)
    if size > pattern_len:
        # Calculate how many times to repeat pattern
        # Ceiling division: equivalent to math.ceil(size / pattern_len)
        repeat_amt: int = -(size // -pattern_len)
        letters: str = (pattern * repeat_amt)[size-1::-1]
    else:
        letters: str = pattern[size-1::-1]

    rangoli: list[str] = []

    # Upper half and middle line
    for line_nr in range(1, size + 1):

        # Left half + center
        left_part: str = fill.join(letters[:line_nr])

        line: str = left_part + left_part[-2::-1]
        width: int = size * 4 - 3
        rangoli.append(line.center(width, fill))

    # Lower half
    for line_nr in range(size - 2, -1, -1):
        rangoli.append(rangoli[line_nr])

    logger.debug("Finished rangoli construction of size %s.", size)

    return '\n'.join(rangoli)

def validate_inputs(
    size: int,
    fill: str = '-',
    pattern: str = 'abcdefghijklmnopqrstuvwxyz',
    max_size: int = 26,
    /) -> None:
    """Validates the user inputs for building an Alphabet Rangoli.

    Args:
        size (int): The size (amount of different letters) of the Rangoli.
        fill (str, optional): The fill to use. Must be a single character. Defaults to '-'.
        pattern (str, optional): The base characters to build the pattern with.  Cannot be empty.
                                 Defaults to the lowercase english alphabet
                                 'abcdefghijklmnopqrstuvwxyz'.
        max_size (int, optional): The maximum number of different letters. Defaults to 26.

    Raises:
        TypeError: If inputs are of the wrong type.
        AlphabetRangoliValidationError: If size is not positive (size > 0).
        AlphabetRangoliValidationError: If max_size is not positive (max_size > 0).
        AlphabetRangoliValidationError: If size exceeds max_size.
        AlphabetRangoliValidationError: If fill or pattern are empty.
    """

    logger.debug("Starting input validation.")

    # Check types
    if not isinstance(size, int):
        raise TypeError(f"size must be of int type, got {type(size).__name__}.")
    if not isinstance(fill, str):
        raise TypeError(f"fill must be of str type, got {type(fill).__name__}.")
    if not isinstance(pattern, str):
        raise TypeError(f"pattern must be of str type, got {type(pattern).__name__}.")
    if not isinstance(max_size, int):
        raise TypeError(f"max_size must be of int type, got {type(max_size).__name__}.")

    # Check bounds
    if size < 1:
        raise AlphabetRangoliValidationError(f"size must be positive (size > 0), got {size}.")
    if max_size < 1:
        raise AlphabetRangoliValidationError(
            f"max_size must be positive (max_size > 0), got {max_size}."
        )
    if size > max_size:
        raise AlphabetRangoliValidationError(
            f"size of {size} exceeds max_size of {max_size}. "
            "Input a valid size or increase max_size."
        )

    # Check fill and pattern
    if len(fill) != 1:
        raise AlphabetRangoliValidationError(
            "fill must be a single character. Please provide one character."
        )
    if not pattern:
        raise AlphabetRangoliValidationError(
            "pattern cannot be empty. Please provide at least one character."
        )

def print_rangoli(
    size: int,
    fill: str = '-',
    pattern: str = 'abcdefghijklmnopqrstuvwxyz',
    max_size: int = 26,
    validate: bool = True,
    /) -> None:
    """Prints an Alphabet Rangoli of the given size.

    Args:
        size (int): The size (amount of different letters) of the Rangoli.
        fill (str, optional): The fill to use. Must be a single character. Defaults to '-'.
        pattern (str, optional): The base characters to build the pattern with.  Cannot be empty.
                                 Defaults to the lowercase english alphabet
                                 'abcdefghijklmnopqrstuvwxyz'.
        max_size (int, optional): The maximum number of different letters. Defaults to 26.
        validate (bool, optional): Whether to validate inputs. Defaults to True.

    Raises:
        TypeError: If inputs are of the wrong type.
        AlphabetRangoliValidationError: If size is not positive (size > 0).
        AlphabetRangoliValidationError: If max_size is not positive (max_size > 0).
        AlphabetRangoliValidationError: If size exceeds max_size.
        AlphabetRangoliValidationError: If fill or pattern are empty.

    Examples:
        >>> print_rangoli(3)
        ----c----
        --c-b-c--
        c-b-a-b-c
        --c-b-c--
        ----c----

        >>> print_rangoli(1)
        a

        >>> print_rangoli(3, fill='.', pattern='012')
        ....2....
        ..2.1.2..
        2.1.0.1.2
        ..2.1.2..
        ....2....

    Notes:
        - Total lines: 2 * size - 1.
        - Line width: 4 * size - 3.
        - Pattern is vertically and horizontally symmetric.
        - If size > len(pattern), the pattern is repeated as needed.
        - Time complexity O(size^2).
        - Space complexity O(size^2).
    """

    print(build_rangoli(size, fill, pattern, max_size, validate))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
