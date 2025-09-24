"""itertools.permutations()

    https://www.hackerrank.com/challenges/itertools-permutations/problem
    """

from itertools import permutations

def validate(inputs: list) -> None:
    """Validates the inputs according to the problem's constraints.
    
    :param list inputs: The input list.
    
    Raises:
        ValueError: If the amount of inputs is not 2.
        TypeError: If the second input is not an integer.
    """

    if not isinstance(inputs, list) or len(inputs) != 2:
        raise ValueError("Expected 2 arguments.")    
    try:
        int(inputs[1])
    except Exception as e:
        raise TypeError(f"Expected an integer as permutation size argument: {e}") from e

def main() -> None:
    """Main function. Handles input and creates the permutations."""

    user_inputs = input().strip().split()
    validate(user_inputs)

    perms = permutations(sorted(user_inputs[0]), int(user_inputs[1]))

    for perm in perms:
        print("".join(perm))

if __name__ == "__main__":
    main()
