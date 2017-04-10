import sys


def dfs(bf, visited, end, i, r):
    if not visited[i]:
        visited[i] = True
        dfs(bf, visited, end, bf[i], r)
        visited[i] = False
    else:
        if bf[bf[i]] == i:
            end[bf[i]] = max(end[bf[i]], len([v for v in visited if v]))
        elif i == r:
            end[i] = max(end[i], len([v for v in visited if v]))
        else:
            end[i] = 0


def solve():
    n = int(input())
    bf = [0] + list(map(int, input().split()))
    end = [0] * (n + 1)
    for i in range(1, n + 1):
        dfs(bf, [False] * (n + 1), end, i, i)
    for i in range(1, n + 1):
        if bf[bf[i]] == i:
            end.append(end[i] + end[bf[i]] - 2)
    end.append(int(sum(end[n + 1:]) / 2))
    return max(end)


def main():
    sys.setrecursionlimit(1500)
    for t in range(int(input())):
        print('Case #{}: {}'.format(t + 1, solve()))


if __name__ == '__main__':
    main()
