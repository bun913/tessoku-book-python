# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A = arrange()
    act(N, A)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A


def act(N, A):
    # 位置関係を求める問題だ
    # ただし、同じ数である場合は、出力する数も同じにしないといけない
    # 出現回数をメモする
    memo = {}
    for a in A:
        memo[a] = 0
    ans = []
    S = sorted(set(A))
    for target in A:
        ind = bisect(target, S)
        ans.append(ind+1)
    print(*ans)


def bisect(target, S):
    ng = -1
    ok = len(S)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(target, S[mid]):
            ok = mid
        else:
            ng = mid
    return ok


def is_ok(target, cur):
    return cur >= target


solve()
