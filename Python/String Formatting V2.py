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

def to_octal(number: int) -> int:
    """Converts the given integer to octal.
    
    :param int number: The number to be converted.
    :return int: The octal conversion.
    """

    octal: int = 0
    count: int = 0
    while number > 0:
        octal = (number % 8) * (10 ** count) + octal
        count += 1
        number = number // 8
    return octal

def to_hex(number: int) -> str:
    """Converts the given integer to hexadecimal.
    
    :param int number: The number to be converted.
    :return str: The hexadecimal conversion.
    """

    hex_digits = "0123456789ABCDEF"
    
    hexadecimal: str = ""
    while number > 0:
        hexadecimal = (hex_digits[number % 16]) + hexadecimal
        number = number // 16
    return hexadecimal
    
def to_bin(number: int) -> int:
    """Converts the given integer to binary.
    
    :param int number: The number to be converted.
    :return int: The binary conversion.
    """

    binary: int = 0
    count: int = 0
    while number > 0:
        binary = (number % 2) * (10 ** count) + binary
        count += 1
        number = number // 2
    return binary

def print_formatted(number: int) -> None:
    """Prints the numbers from 1 to the given number in decimal, octal, hexadecimal and binary.

    :param int number: the maximum number to print.
    """

    validate(number)

    col_w = len(str(to_bin(number)))
    
    for decimal in range(1, number + 1):
        print(f"{decimal:>{col_w}} {to_octal(decimal):>{col_w}} {to_hex(decimal):>{col_w}} {to_bin(decimal):>{col_w}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
