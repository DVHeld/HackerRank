"""itertools.combinations()

    https://www.hackerrank.com/challenges/itertools-combinations/problem
    """

from itertools import combinations

def validate(user_input: list[str]) -> None:
    """Validates the input according to the constrains.
    
    :param list[str] user_input: The input to be validated.

    Raises:
        ValueError: If there amount of inputs is different than 2.
        TypeError: If the length of the combination is not an integer.
        ValueError: If the string's length is shorter than the combination's length.
    """

    if not isinstance(user_input, list) or len(user_input) != 2:
        raise ValueError("Expected eaxctly 2 inputs.")
    try:
        n: int = int(user_input[1])
    except Exception as e:
        raise TypeError(f"Expected an integer as the second input: {e}") from e
    if len(user_input[0]) < n:
        raise ValueError("The string's length must be greater or equal to the combination's length.")

def main() -> None:
    """Main function. Handles input, validation and generates the combinations."""

    user_input: list[str] = input().strip().split()
    validate(user_input)
    input_string = sorted(user_input[0].strip())
    for i in range(1, int(user_input[1]) + 1):
        combos = combinations(input_string, i)
        for combo in combos:
            print(''.join(combo))

if __name__ == "__main__":
    main()
