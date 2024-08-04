# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    N, K, L, R = arrange()
    act(L, R, K)


def arrange():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    l = A[:len(A)//2]
    r = A[len(A)//2:]
    # 前半の取りうる合計値を列挙する
    L = bit_full_search(l)
    R = bit_full_search(r)
    L.sort()
    R.sort()
    return N, K, L, R


def bit_full_search(lis):
    n = len(lis)
    array = []
    for i in range(2**n):
        tmp = 0
        for j in range(n):
            if 1 & (i >> j):
                tmp += lis[j]
        array.append(tmp)
    return array


def act(L, R, K):
    for l in L:
        target = K - l
        ind = bisect(R, target)
        if ind >= 0 and ind < len(R):
            if R[ind] == target:
                print("Yes")
                exit()
    print("No")


def bisect(R, target):
    ng = -1
    ok = len(R)
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(R[mid], target):
            ok = mid
        else:
            ng = mid
    return ok


def is_ok(r, target):
    return r >= target


solve()
