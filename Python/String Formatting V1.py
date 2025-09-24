"""String Formatting

    https://www.hackerrank.com/challenges/python-string-formatting/problem
    """

def validate(number: int) -> None:
    """Validates the input.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is < 1.
    """

    if not isinstance(number, int):
        raise TypeError("Expected a positive integer.")
    if number < 1:
        raise ValueError("Expected a positive integer.")

def print_formatted(number: int) -> None:
    """Prints the numbers from 1 to the given number in decimal, octal, hexadecimal and binary.

    :param int number: the maximum number to print.
    """

    validate(number)

    col_w = len(bin(number)[2:])

    for d in range(1, number + 1):
        print(f"{d:>{col_w}} {d:>{col_w}o} {d:>{col_w}X} {d:>{col_w}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
