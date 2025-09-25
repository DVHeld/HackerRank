"""itertools.combinations_with_replacement()

    https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
    """

from itertools import combinations_with_replacement

def validate(user_input: list[str]) -> None:
    """Validates the input according to the constraints.

    :param list[str] user_input: The input to be validated.
    
    Raises:
        ValueError: If the input amount is different than 2.
        TypeError: If the combination length is not an integer.
        ValueError: If the input string is shorter than the combination length.
    """

    if not isinstance(user_input, list) or len(user_input) != 2:
        raise ValueError("Expected exactly 2 inputs.")
    try:
        n = int(user_input[1])
    except Exception as e:
        raise TypeError(f"Expected an integer as second input: {e}") from e
    if len(user_input[0]) < n:
        raise ValueError("The input string must be longer or equal to the combination length.")

def main() -> None:
    """Main funcion. Handles input, validates it and generates the combinations."""

    user_input = input().strip().split()
    validate(user_input)

    input_string = sorted(user_input[0])
    combo_len = int(user_input[1])
    combos = combinations_with_replacement(input_string, combo_len)
    for combo in combos:
        print(''.join(combo))

if __name__ == '__main__':
    main()
