"""Find a string

    https://www.hackerrank.com/challenges/find-a-string/problem
    """

def validate(string: str, sub_string: str, /) -> None:
    """Validates user input according to the problem's restrictions.

    Args:
        string (str): The input string.
        sub_string (str): The input substring.

    Raises:
        ValueError: If string or substring length exceeds bounds.
        ValueError: If string or substring conain non-ascii characters
    """

    if not 1 <= len(string) <= 200:
        raise ValueError("String length exceeds bounds.")
    if not 1 <= len(sub_string) <= len(string):
        raise ValueError("Substring length exceeds bounds.")
    for index, char in enumerate(string):
        if not char.isascii():
            raise ValueError(f"String conains non-ascii characters: {char} at index {index}.")
    for index, char in enumerate(sub_string):
        if not char.isascii():
            raise ValueError(f"Substring conains non-ascii characters: {char} at index {index}.")

def count_substring(string: str, sub_string: str, /) -> int:
    """Counts the amount of times sub_string occurs in string and returns the result.

    Args:
        string (str): The input string.
        sub_string (str): The substring to find.

    Returns:
        int: The resulting count.
    """

    validate(string, sub_string)

    count: int = 0
    for index in range(1 + len(string) - len(sub_string)):
        if sub_string == string[index:index + len(sub_string)]:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
