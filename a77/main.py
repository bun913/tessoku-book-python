# -*- coding: utf-8 -*-
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, L, K, A = arrange()
    act(N, L, K, A)


def arrange():
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))
    return N, L, K, A


def act(N, L, K, A):
    ok = -1  # 最大のxを求めたいので、okを左側にする
    ng = L + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, K, A, L):
            ok = mid
        else:
            ng = mid
    print(ok)


def is_ok(length, K, A, L):
    cnt, last = 0, 0
    for i in range(len(A)):
        a = A[i]
        # そこで切った左側と右側の長さがlength以上であれば、切る
        if a - last >= length and L - a >= length:
            cnt += 1
            last = a
    if cnt >= K:
        return True
    return False


solve()
