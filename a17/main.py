# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, A, B = arrange()
    dp = dpfn(N, A, B)
    act(N, dp, A, B)


def arrange():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    return N, A, B


def dpfn(N, A, B):
    dp = [0] * N
    dp[1] = A[0]
    dp[2] = min(A[0] + A[1], B[0])
    for i in range(3, N):
        cand1 = dp[i-1] + A[i-1]
        cand2 = dp[i-2] + B[i-2]
        dp[i] = min(cand1, cand2)
    return dp


def act(N, dp, A, B):
    place = N-1
    ans = []
    # この実装方法添字がバグらなくて良いな
    # 現在位置の方を減らしていくスタイル
    while True:
        ans.append(place+1)
        if place == 0:
            break
        if dp[place] == dp[place-1] + A[place-1]:
            place -= 1
        else:
            place -= 2
    ans = ans[::-1]
    print(len(ans))
    print(*ans, sep=" ")


solve()
