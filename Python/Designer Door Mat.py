"""Designer Door Mat

    https://www.hackerrank.com/challenges/designer-door-mat/problem
    """

def print_line(line_nr: int, N: int, M: int) -> None:
    """Print the design line corresponding to line_nr for a design of length N and width M.
    
    :param int line_nr: The line number to generate and print.
    :param int N: The design's length.
    :param int M: The design's width.
    """

    # Design elements
    FILL = ".|."
    DASH = "-"
    WORD = "WELCOME"

    middle = N // 2

    if line_nr == middle:
        dash_amt = (M - len(WORD)) // 2
        line = DASH * dash_amt + WORD + DASH * dash_amt
    else:
        distance_from_middle = abs(middle - line_nr)
        fill_amt = 1 + 2 * (middle - distance_from_middle)
        dash_amt = (M - fill_amt * len(FILL)) // 2
        line = DASH * dash_amt + FILL * fill_amt + DASH * dash_amt
    print(line)

def validate(N: int, M: int) -> None:
    """Validates the input parameters according to the design's constraints.
    
    :param int N: The design's length.
    :param int M: The design's width.
    
    Raises:
       ValueError: If the inputs don't conform to the design's constraints. 
    """

    if N % 2 == 0:
        raise ValueError("Height must be odd.")
    if M % 2 == 0:
        raise ValueError("Width must be odd.")
    if M != 3 * N:
        raise ValueError("Width must be three times the height.")

def create_mat(N: int, M: int) -> None:
    """Assembles the mat.
    
    :param int N: The mat's length. Odd number.
    :param int M: The mat's width. 3 times N.
    :return: None
    """

    validate(N, M)
    for line_nr in range(N):
        print_line(line_nr, N, M)

def main():
    """Main function to handle input and create mat."""

    try:
        user_input = input().strip().split()

        if len(user_input) != 2:
            raise ValueError("Expected exactly 2 space-separated integers.")

        N, M = int(user_input[0]), int(user_input[1])
        create_mat(N, M)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()
