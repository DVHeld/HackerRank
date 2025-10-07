"""Find a string

    https://www.hackerrank.com/challenges/find-a-string/problem

    Substring counting module with production-grade validation, error handling and functionality.

    This module provides robust overlapping substring counting functionality with substring location, comprehensive
    input validation, batch processing and fault-tolerant variants.

    Classes:
        SubstringCountError: Base exception for substring counting errors.
        ValidationError: Raised when input validation fails.

    Functions:
        count_substring: Counts the amount of occurrences of substring in string, including overlapping matches.
        count_substring_safe: Safe version that returns default value on error instead of raising.
        count_substring_batch: Count substring in multiple strings (batch processing).
        find_all_positions: Returns a list of all the positions at which the substring is found within the string, including overlapping ones.
        validate_inputs: Validates user inputs for substring counting.
    """

__all__ = [
    'SubstringCountError',
    'ValidationError',
    'count_substring',
    'count_substring_safe',
    'count_substring_batch',
    'find_all_positions',
    'validate_inputs'
]

import logging
from typing import Optional

logger = logging.getLogger(__name__)

if not logger.handlers:
    logger.addHandler(logging.NullHandler())

class SubstringCountError(Exception):
    """Base exception for substring counting errors."""
    pass

class ValidationError(SubstringCountError):
    """Raised when input validation fails."""
    pass

def validate_inputs(
    string: str,
    sub_string: str,
    max_len: int = 200,
    require_ascii: bool = True,
    allow_empty_substring: bool = False,
    /) -> None:
    """Validates user inputs for substring counting.

    Args:
        string (str): The string to check in.
        sub_string (str): The string to look for.
        max_len (int, optional): The maximum allowed string length. Defaults to 200.
        require_ascii (bool, optional): Whether to only allow ascii characters. Defaults to True.
        allow_empty_substring (bool, optional): Whether to allow an empty substring. Defaults to False.

    Raises:
        TypeError: If string is not of type str.
        TypeError: If sub_string is not of type str.
        TypeError: If max_len is not of type int.
        TypeError: If require_ascii is not of type bool.
        TypeError: If allow_empty_substring is not of type bool.
        ValidationError: If max_len is not positive.
        ValidationError: If string is empty.
        ValidationError: If string length exceeds the maximum of max_len.
        ValidationError: If sub_string is empty.
        ValidationError: If sub_string length exceeds string length.
        ValidationError: If string contains forbidden non-ascii characters.
        ValidationError: If sub_string contains forbidden non-ascii characters.
    """

    logger.debug("Validating inputs.")

    # Type validation
    if not isinstance(string, str):
        raise TypeError(
            f"string must be of type str, got {type(string).__name__}. "
            f"Received value: {repr(string)}."
            )

    if not isinstance(sub_string, str):
        raise TypeError(
            f"sub_string must be of type str, got {type(sub_string).__name__}. "
            f"Received value: {repr(sub_string)}."
            )

    if not isinstance(max_len, int):
        raise TypeError(
            f"max_len must be of type int, got {type(max_len).__name__}. "
            f"Received value: {repr(max_len)}."
            )

    if not isinstance(require_ascii, bool):
        raise TypeError(
            f"require_ascii must be of type bool, got {type(require_ascii).__name__}. "
            f"Received value: {repr(require_ascii)}."
            )

    if not isinstance(allow_empty_substring, bool):
        raise TypeError(
            f"allow_empty_substring must be of type bool, got {type(allow_empty_substring).__name__}. "
            f"Received value: {repr(allow_empty_substring)}."
            )

    # max_len validation
    if max_len < 1:
        raise ValidationError(f"max_len must be positive, got {max_len}.")

    # Length constraints validation
    str_len = len(string)
    if str_len == 0:
        raise ValidationError(
            "string cannot be empty. "
            "Provide a non-empty string to search in."
            )
    if str_len > max_len:
        raise ValidationError(
            f"string length ({str_len}) exceeds maximum of {max_len}. "
            f"Consider processing in chunks or increasing max_len."
            )

    substr_len = len(sub_string)
    if substr_len == 0 and not allow_empty_substring:
        raise ValidationError(
            "sub_string cannot be empty. "
            "Provide a non-empty string to search for or set allow_empty_substring to True."
            )
    if substr_len > str_len:
        raise ValidationError(
            f"sub_string length ({substr_len}) cannot exceed string length ({str_len}). "
            f"Substring: {repr(sub_string[:50])}{'...' if substr_len > 50 else ''}"
            )

    # ASCII-only validation
    if require_ascii:
        try:
            string.encode('ascii')
        except UnicodeEncodeError as e:
            for index, character in enumerate(string):
                if not character.isascii():
                    raise ValidationError(
                        f"string contains forbidden non-ascii character '{repr(character)}' "
                        f"(Unicode: U+{ord(character):04X}) at position {index}. "
                        "Only ASCII characters are allowed. "
                        "Consider setting require_ascii to False."
                        ) from e
        try:
            sub_string.encode('ascii')
        except UnicodeEncodeError as e:
            for index, character in enumerate(sub_string):
                if not character.isascii():
                    raise ValidationError(
                        f"sub_string contains forbidden non-ascii character '{repr(character)}' "
                        f"(Unicode: U+{ord(character):04X}) at position {index}. "
                        f"Only ASCII characters are allowed. "
                        f"Consider setting require_ascii to False."
                        ) from e

    logger.debug("Input validation passed: str_len=%s, substr_len=%s.", str_len, substr_len)

def find_all_positions(
    string: str,
    sub_string: str,
    max_len: int = 200,
    require_ascii: bool = True,
    allow_empty_substring: bool = False,
    validate: bool = True,
    /) -> list[int]:
    """Returns a list of all the positions at which the substring is found within the string, including overlapping ones.

    Args:
        string (str): The string to check in.
        sub_string (str): The string to look for.
        max_len (int, optional): The maximum allowed string length. Defaults to 200.
        require_ascii (bool, optional): Whether to only allow ascii characters. Defaults to True.
        allow_empty_substring (bool, optional): Whether to allow an empty substring. Defaults to False.
        validate (bool, optional): Whether to do validation checks. Defaults to True.

    Raises:
        TypeError: If validate is not of type bool.
        ValidationError: If validation constraints are violated.

    Returns:
        list[int]: A list containing the positions of every occurrence of substring in the string.
    
    Examples:
        >>> find_all_positions("AAAA", "AA")
        [0, 1, 2]
        >>> find_all_positions("ABCDCDC", "CDC")
        [2, 4]

    Notes:
        - Returns 0-based indices.
        - Includes overlapping matches.
        - Time complexity: O(n*m) where n = len(string) and m = len(sub_string).
        - Space complexity: O(k) where k = number of matches. 
    """

    if not isinstance(validate, bool):
        raise TypeError(
            f"validate must be of type bool, got {type(validate).__name__}. "
            f"Received value: {repr(validate)}."
            )

    if validate:
        validate_inputs(
            string,
            sub_string,
            max_len,
            require_ascii,
            allow_empty_substring
        )

    substr_len: int = len(sub_string)
    str_len: int = len(string)

    logger.debug("Started search for substring %s in string of length %s.",
        repr(sub_string[:50]) + ('...' if len(sub_string) > 50 else ''),
        str_len
    )
    positions: list[int] = [index for index in range(len(string) - substr_len + 1) if sub_string == string[index:index + substr_len]]

    occurrences: int = len(positions)
    logger.debug(
        "Found %s occurrence%s at position%s: %s.",
        occurrences,
        's' if occurrences != 1 else '',
        's' if occurrences != 1 else '',
        positions
    )
    return positions

def count_substring_safe(
    string: Optional[str],
    sub_string: Optional[str],
    default: int = 0,
    max_len: int = 200,
    require_ascii: bool = True,
    allow_empty_substring: bool = False,
    validate: bool = True,
    /) -> int:
    """Safe version that returns default value on error instead of raising.

    Useful for ETL pipelines or for data processing when you want to continue even if some inputs are invalid.

    Args:
        string (Optional[str]): The string to check in.
        sub_string (Optional[str]): The string to look for.
        default (int, optional): The default value to return. Defaults to 0.
        max_len (int, optional): The maximum allowed string length. Defaults to 200.
        require_ascii (bool, optional): Whether to only allow ascii characters. Defaults to True.
        allow_empty_substring (bool, optional): Whether to allow an empty substring. Defaults to False.
        validate (bool, optional): Whether to do validation checks. Defaults to True.

    Raises:
        TypeError: If default is not of type int.

    Returns:
        int: The amount of occurrences, or default value if validation fails.

    Notes:
        - Case-sensitive.
        - Counts overlapping matches.
        - Never raises exceptions (except for invalid default parameter).
        - Logs warnings for validation failures.
        - Logs errors with stack traces for unexpected failures.
        - Useful for data pipelines where robustness is critical.
        - Time complexity O(n*m) where n = len(string) and m = len(sub_string)
        - Space complexity O(1)

    Examples:
        >>> count_substring("AAAA", "AA")
        3
        >>> count_substring("", "AA")
        0
        >>> count_substring("test", None, default=-1)
        -1
    """

    if not isinstance(default, int):
        raise TypeError(
            f"Expected default to be of type int, got {type(default).__name__}. "
            f"Received value: {repr(default)}."
            )

    try:
        if string is None or sub_string is None:
            logger.warning("Received None input, returning default value.")
            return default

        return count_substring(
            string,
            sub_string,
            max_len,
            require_ascii,
            allow_empty_substring,
            validate
        )

    except (TypeError, ValidationError) as e:
        logger.warning("Validation failed: %s. Returning default value.", e)
        return default

    except Exception as e: # pylint: disable=broad-exception-caught
        logger.error(
            "Unexpected error in count_substring_safe: %s. Returning default value.",
            e,
            exc_info=True
        )
        return default

def count_substring_batch(
    string_list: list[str],
    sub_string: str,
    skip_invalid: bool = True,
    max_len: int = 200,
    require_ascii: bool = True,
    allow_empty_substring: bool = False,
    validate: bool = True,
    /) -> list[int]:
    """Count substring in multiple strings (batch processing).

    Args:
        string_list (list[str]): The list of strings to check in.
        sub_string (str): The string to look for.
        skip_invalid (bool, optional): Whether to skip invalid strings. Defaults to True.
        max_len (int, optional): The maximum allowed string length. Defaults to 200.
        require_ascii (bool, optional): Whether to only allow ascii characters. Defaults to True.
        allow_empty_substring (bool, optional): Whether to allow an empty substring. Defaults to False.
        validate (bool, optional): Whether to do validation checks. Defaults to True.

    Raises:
        TypeError: If string_list is not of type list.
        TypeError: If skip_invalid is not of type bool.
        ValidationError: If string_list is empty.
        ValidationError: If a string is invalid and skip_invalid is set to False. 

    Returns:
        list[int]: List of counts corresponding to each string input.
    
    Examples:
        >>> count_substring_batch(["AAA", "BBB", "AAABAA"], "AA")
        [2, 0, 3]
    """

    # Type check
    if not isinstance(string_list, list):
        raise TypeError(
            f"Expected string_list to be of type list, got {type(string_list).__name__}. "
            f"Received value: {repr(string_list)}."
            )

    if not isinstance(skip_invalid, bool):
        raise TypeError(
            f"Expected skip_invalid to be of type bool, got {type(skip_invalid).__name__}. "
            f"Received value: {repr(skip_invalid)}."
            )

    # Empty list check
    if len(string_list) == 0:
        raise ValidationError(
            "Received empty list as string_list."
        )

    # Process list
    logger.debug("Starting batch processing of list of length %s for substring: %s.",
        len(string_list),
        repr(sub_string[:50]) + '...' if len(sub_string) > 50 else ''
        )
    results: list[int] = []
    for index, string in enumerate(string_list):
        try:
            count: int = count_substring(
                string,
                sub_string,
                max_len,
                require_ascii,
                allow_empty_substring,
                validate
            )
            results.append(count)
        except (TypeError, ValidationError) as e:
            if skip_invalid:
                logger.warning("Skipping invalid string at index %s: %s.", index, e)
                results.append(0)
            else:
                raise ValidationError(f"Invalid string at index {index}: {e}.") from e

    return results

def count_substring(
    string: str,
    sub_string: str,
    max_len: int = 200,
    require_ascii: bool = True,
    allow_empty_substring: bool = False,
    validate: bool = True,
    /) -> int:
    """Counts the amount of occurrences of substring in string, including overlapping matches.

    It sequentially scans through the string, checking for matches. 

    Args:
        string (str): The string to check in.
        sub_string (str): The string to look for.
        max_len (int, optional): The maximum allowed string length. Defaults to 200.
        require_ascii (bool, optional): Whether to only allow ascii characters. Defaults to True.
        allow_empty_substring (bool, optional): Whether to allow an empty substring. Defaults to False.
        validate (bool, optional): Whether to do validation checks. Defaults to True.

    Returns:
        int: The match count.

    Raises:
        TypeError: If validate is not of type bool.

    Notes:
        - Case-sensitive.
        - Counts overlapping matches.
        - Time complexity O(n*m) where n = len(string) and m = len(sub_string)
        - Space complexity O(1)

    Examples:
        >>> count_substring("AAB", "AA")
        1
        >>> count_substring("AAAA", "AA")
        3
        >>> count_substring("ABCDCDC", "CDC")
        2
        >>> count_substring("ABC", "x")
        0
        >>> count_substring("", "AA") # Raises ValidationError
    """

    if not isinstance(validate, bool):
        raise TypeError(
            f"validate must be of type bool, got {type(validate).__name__}. "
            f"Received value: {repr(validate)}."
            )

    if validate:
        validate_inputs(
            string,
            sub_string,
            max_len,
            require_ascii,
            allow_empty_substring
            )

    str_len = len(string)
    substr_len = len(sub_string)
    if substr_len > str_len:
        logger.warning(
            "substr_len (%s) > str_len (%s). Returning 0.",
            substr_len,
            str_len
        )
        return 0

    logger.debug(
        "Counting '%s' in string of length %s.",
        sub_string,
        len(string)
    )

    count = sum(1 for index in range(1 + str_len - substr_len) if sub_string == string[index:index + substr_len])

    logger.debug(
        "Found %s occurrence%s of substring %s in string of length %s.",
        count,
        's' if count != 1 else '',
        repr(sub_string[:50]) + '...' if substr_len > 50 else '',
        str_len
    )
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
