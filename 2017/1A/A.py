def solve():
    r, c = map(int, input().split())
    rows = [list(input()) for i in range(r)]

    for i in range(r):
        for j in range(1, c):
            if rows[i][j] == '?':
                rows[i][j] = rows[i][j - 1]
    for i in range(r):
        for j in range(c - 2, -1, -1):
            if rows[i][j] == '?':
                rows[i][j] = rows[i][j + 1]

    for i in range(1, r):
        if rows[i][0] == '?':
            rows[i] = rows[i - 1][:]

    for i in range(r - 2, -1, -1):
        if rows[i][0] == '?':
            rows[i] = rows[i + 1][:]

    return '\n'.join(map(lambda x: ''.join(x), rows))


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1))
        print(solve())


if __name__ == '__main__':
    main()
