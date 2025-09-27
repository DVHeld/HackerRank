"""String Split and Join

    https://www.hackerrank.com/challenges/python-string-split-and-join/problem
    """
def split_and_join(line):
    """Replaces the line's ' ' spaces with dashes '-' through splitting and joining the string.

    Args:
        line (str): The string to raplace the spaces of.

    Returns:
        str: The modified string.
    """

    return '-'.join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
