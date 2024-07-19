# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1]*n

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


setrecursionlimit(10**8)


def solve():
    N, Q = arrange()
    act(N, Q)


def arrange():
    return map(int, input().split())


def act(N, Q):
    uf = UnionFind(N)
    for _ in range(Q):
        q, a, b = map(int, input().split())
        if q == 1:
            uf.merge(a-1, b-1)
            continue
        if uf.same(a-1, b-1):
            print("Yes")
        else:
            print("No")


solve()
