"""Find the Runner-Up Score!

    https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
    """

if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()), reverse=True)
    last = arr[0]
    for i in arr[1:]:
        if i != last:
            print(i)
            break