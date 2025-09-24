"""Lists

    https://www.hackerrank.com/challenges/python-lists/problem
    """

def validate(N: int) -> None:
    """Validates the user input.

    :param int N: The input.
    
    Raises:
        ValueError: If the input is < 1."""

    if N < 1:
        raise ValueError("Expected a positive non-zero integer.")

if __name__ == '__main__':
    N: int = int(input())
    validate(N)
    user_input: list = []
    array: list = []
    for _ in range(N):
        user_input = input().strip().split()
        if user_input[0] == "insert":
            array.insert(int(user_input[1]), int(user_input[2]))
        elif user_input[0] == "print":
            print(array)
        elif user_input[0] == "remove":
            array.remove(int(user_input[1]))
        elif user_input[0] == "append":
            array.append(int(user_input[1]))
        elif user_input[0] == "sort":
            array.sort()
        elif user_input[0] == "pop":
            array.pop()
        elif user_input[0] == "reverse":
            array.reverse()
        else:
            print("Unexpected input. Try again.")
