"""Tuples

    https://www.hackerrank.com/challenges/python-tuples/problem
    """

def validate(n, user_input):
    """Validates the input.
    
    :param int n: The input.
    
    Raises:
        ValueError: If the input is < 1.
    """

    if n < 1:
        raise ValueError("Expected a positive non-zero integer.")
    if n != len(user_input):
        raise ValueError("Expected a positive non-zero integer.")
    for number in user_input:
        try:
            number = int(number)
        except Exception as e:
            raise TypeError("Expected a positive non-zero integer.")

def main():
    """Main block. Handles input, builds the tuple, computes the hash
    and prints the result."""

    input_count = input()
    try:
        input_count = int(input_count)
    except Exception as e:
        raise TypeError("Expected a positive non-zero integer.")
    user_input = raw_input().strip().split()
    validate(input_count, user_input)

    input_tuple = tuple(int(num) for num in user_input)
    print(hash(input_tuple))

if __name__ == "__main__":
    main()
