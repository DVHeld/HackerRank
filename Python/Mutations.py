"""Mutations

    https://www.hackerrank.com/challenges/python-mutations/problem
    """

def validate(string: str, position: int, character: str, /) -> None:
    """Validates the user input.

    Args:
        string (str): The input string.
        position (int): The input position.
        character (str): The input character.

    Raises:
        IndexError: Position is out of the range 0 < position < len(string).
        ValueError: If the character string is not a single character.
    """

    if not 0 < position < len(string):
        raise IndexError(f"Position {position} out of range.")
    if len(character) != 1:
        raise ValueError("Character must be a single string.")

def mutate_string(string: str, position: int, character: str, /) -> str:
    """Replaces the character at the given position with the given character

    Args:
        string (str): The string where the chatacter will be replaced in.
        position (int): The position of the character to be replaced.
        character (str): The character to insert.

    Returns:
        str: The modified string.
    """

    assert isinstance(string, str), "Expected a string."
    assert isinstance(position, int), "Expected an integer."
    assert isinstance(character, str), "Expected a string."
    validate(string, position, character)
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
