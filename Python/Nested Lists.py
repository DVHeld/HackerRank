"""Nested Lists

    https://www.hackerrank.com/challenges/nested-list/problem
    """

from operator import itemgetter

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        records.append([input(), float(input())])
    
    records = sorted(records, key=itemgetter(0))
    slg = sorted(list(set(grade[1] for grade in records)))[1]
    for record in records:
        if record[1] == slg:
            print(record[0])
