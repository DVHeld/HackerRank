"""sWAP cASE

    https://www.hackerrank.com/challenges/swap-case/problem
    """

def validate(input_string: str, /) -> None:
    """Validates the user input according to the problem's constraints.
    
    Params:
        input_string: The user input to be validated.
    """

    if not 0 < len(input_string) <= 1000:
        raise ValueError(f"Expected input length of 0 < len(input_string) <= 1000, was {len(input_string)}.")

def swap_case(input_string: str, /) -> str:
    """Swaps the string's cases from lower-case to upper-case and vice-versa.

    Params:
        input_string: The input string to be swap-cased.

    Returns:
        str: The swap-cased string.
    """

    validate(input_string)

    swapped: str = ''
    for char in input_string:
        if char.islower():
            swapped = swapped + char.upper()
        elif char.isupper():
            swapped = swapped + char.lower()
        else:
            swapped = swapped + char
    return swapped

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
