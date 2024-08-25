# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    X, Y = arrange()
    act(X, Y)


def arrange():
    return map(int, input().split())


def act(X, Y):
    # 1同士なら何もしなくてもOK
    if X == 1 and Y == 1:
        print(0)
        exit()
    # それ以外はXとYの最大公約数は1という制約がある
    ans = []
    x, y = X, Y
    while x >= 2 or y >= 2:
        ans.append((x, y))
        if x > y:
            x -= y
        else:
            y -= x
    print(len(ans))
    for x, y in reversed(ans):
        print(x, y)


solve()
