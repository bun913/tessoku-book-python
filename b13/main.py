# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, K, A = arrange()
    act(N, K, A)


def arrange():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, A


def act(N, K, A):
    # 累積和を求める
    accum = [0] * (N + 1)
    for i in range(1, N+1):
        accum[i] = accum[i-1] + A[i-1]
    # 尺取り法で条件を満たす区間を調べる
    R = [0] * N
    for i in range(N):
        if i == 0:
            R[i] = -1
        else:
            R[i] = R[i-1]
        while R[i] < N-1 and sum(i, R[i]+1, accum) <= K:
            R[i] += 1
            # 答えを出力
    ans = 0
    for i in range(0, N):
        ans += (R[i] - i + 1)
    print(ans)


def sum(l, r, S):
    return S[r+1] - S[l]


solve()
