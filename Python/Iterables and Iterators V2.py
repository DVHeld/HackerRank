"""Iterables and Iterators

    https://www.hackerrank.com/challenges/iterables-and-iterators/problem
    """

from math import comb

def validate(user_input: list[str], /) -> None:
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
    if not (1 <= N <= 10):
        raise ValueError("N must be 1 <= N <= 10.")
    if not (1 <= K <= N):
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
        if not (97 <= ascii_value <= 122):
            raise ValueError("3: The letter string must be of single lower-case letters separated by single spaces.")

    # Spaces in the string, if formatted correctly.
    spaces = s[1::2]
    if spaces != ' ' * len(spaces):    
        raise ValueError("4: The letter string must be of single lower-case letters separated by single spaces.")

def extract_a_indices(input_string: str, /) -> set[int]:
    """Extracts the location of the letters 'a' contained in the input string.

    Params:
        input_string: The user input string to extract the indices from.

    Returns:
        list[int]: A list containing the indices.
    """

    input_list = input_string.split()
    return {index + 1 for index, char in enumerate(input_list) if char == 'a'}

def calculate_probability(N: int, a_indices: set[int], K: int, /) -> float:
    """Calculates the probability of a combination containing an 'a' index.
    
    Params:
        N: Total position number.
        a_indices: The 'a' indices.
        K: Number of indices to select.
    
    Returns:
        float: The calculated probability.
    """

    not_a = N - len(a_indices)
    if K > not_a:
        return 1.0
    return 1.0 - (comb(not_a, K)/comb(N, K))
 
def main() -> None:
    """Calculates the probability of an index containing the letter 'a'."""

    user_input = [input() for _ in range(3)]
    validate(user_input)

    N: int = int(user_input[0])
    a_indices: set[int] = extract_a_indices(user_input[1])
    K: int = int(user_input[2])

    print(calculate_probability(N, a_indices, K))

if __name__ == "__main__":
    main()
