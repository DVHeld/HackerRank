"""Compress the String!

    https://www.hackerrank.com/challenges/compress-the-string/problem
    """

from itertools import groupby

def validate(input_string: str) -> None:
    """Validates the input

    Args:
        input_string: The user input to validate.

    Raises:
        ValueError: If the input is empty or contains a non-digit character.
    """

    if len(input_string) == 0:
        raise ValueError("Missing input string.")
    for char in input_string:
        if not char.isdigit():
            raise ValueError("All characters must be digits.")

def rle(input_string: str) -> str:
    """Compress consecutive characters using run-length encoding.
    
    Args:
        input_string: The string to be compressed.
    
    Returns:
        The run-length encoded string in format "(count, char) (count, char) ..."
    """

    return ' '.join([f"({sum(1 for _ in group)}, {char})" for char, group in groupby(input_string)])

def main() -> None:
    """Encondes the input string using run-length encoding."""

    input_string: str = input().strip()
    validate(input_string)
    print(rle(input_string))

if __name__ == "__main__":
    main()
