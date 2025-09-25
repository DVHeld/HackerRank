"""String Formatting

    https://www.hackerrank.com/challenges/python-string-formatting/problem
    """

from itertools import combinations

def validate(user_input: list[str]) -> None:
    """Validates the user input according to the constraints.

    Params:
        user_input: The list of user inputs to validate.

    Raises:
        TypeError: If N or K are not integers.
        ValueError: If the string is not composed of single lower-case letters separated by single spaces. Also raised if N is not 1 <= N <= 10 or if K is not 1 <= K <= N. 
    """

    # Check K and N constraints. Must be integers such that 1 <= N <= 10 and 1 <= K <= N.
    try:
        N: int = int(user_input[0])
        K: int = int(user_input[2])
    except Exception as e:
        raise TypeError(f"N and K must be integers: {e}") from e
    if not 1 <= N <= 10:
        raise ValueError("N must be 1 <= N <= 10.")
    if not 1 <= K <= N:
        raise ValueError("K must be 1 <= K <= N.")

    s = user_input[1].strip()
    # Quick check, a valid input's length will be an odd number.
    if len(s) % 2 == 0:
        raise ValueError("1: The letter string must be of single lower-case letters separated by single spaces.")

    # Characters in the string, if formatted correctly.
    chars = s[::2]
    if ' ' in chars:
        raise ValueError("2: The letter string must be of single lower-case letters separated by single spaces.")

    if len(chars) != N:
        raise ValueError(f"Expected {N} letters, got {len(chars)}.")

    # Check if characters are all lower-case english letters.
    for char in chars:
        ascii_value = ord(char)
        if not 97 <= ascii_value <= 122:
            raise ValueError("3: The letter string must be of single lower-case letters separated by single spaces.")

    # Spaces in the string, if formatted correctly.
    spaces = s[1::2]
    if spaces != ' ' * len(spaces):    
        raise ValueError("4: The letter string must be of single lower-case letters separated by single spaces.")

def extract_a_indices(input_string: str) -> set[int]:
    """Extracts the location of the letters 'a' contained in the input string.

    Params:
        input_string: The user input string to extract the indices from.

    Returns:
        list[int]: A list containing the indices.
    """

    input_list = input_string.split()
    return {index + 1 for index, char in enumerate(input_list) if char == 'a'}

def main() -> None:
    """Calculates the probability of an index containing the letter 'a'."""

    user_input = [input() for _ in range(3)]
    validate(user_input)

    N: int = int(user_input[0])
    a_indices: set[int] = extract_a_indices(user_input[1].strip())
    K: int = int(user_input[2])

    p_numerator: int = 0
    index_combos: set[list] = set(combinations(range(1, N + 1), K))
    for combo in index_combos:
        if not a_indices.isdisjoint(combo):
            p_numerator += 1

    print(p_numerator / len(index_combos))

if __name__ == "__main__":
    main()
