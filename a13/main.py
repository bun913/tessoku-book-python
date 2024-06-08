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
    ans = 0
    # R[i]にはどのインデックス番号まで進めるかを格納する
    R = [0 for _ in range(N)]
    for i in range(N):
        if i == 0:
            R[i] = -1
        else:
            # 前の結果を利用するところから始める
            R[i] = R[i-1]
        # 条件を満たすところまで進めてR[i]を更新する
        while R[i] < N-1 and A[R[i]+1] - A[i] <= K:
            R[i] += 1
    # 結果を出力
    ans = 0
    for i in range(0, N-1):
        ans += R[i] - i
    print(ans)


solve()
