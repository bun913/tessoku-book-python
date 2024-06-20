# -*- coding: utf-8 -*-
"""
解く前のメモ用
"""
from sys import setrecursionlimit

setrecursionlimit(10**8)


def solve():
    H, W, K, C = arrange()
    act(H, W, K, C)


def arrange():
    H, W, K = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    return H, W, K, C


def act(H, W, K, C):
    rows, org_cols, total_white = count_white_cells(H, W, C)
    black_cnt = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                black_cnt += 1

    max_ans = 0
    for row_bit in range(1 << H):
        cols = org_cols[:]
        ans = black_cnt
        remain_cnt = K

        # 行を選択し、対応する列の白セル数を更新
        for i in range(H):
            if (row_bit >> i) & 1:
                remain_cnt -= 1
                ans += rows[i]
                for j in range(W):
                    if C[i][j] == '.':
                        cols[j] -= 1

        if remain_cnt < 0:
            continue

        # 列の選択
        cols.sort(reverse=True)
        col_sum = sum(cols[:remain_cnt])
        ans += col_sum
        max_ans = max(max_ans, ans)

    print(max_ans)


def count_white_cells(H, W, C):
    rows = [0] * H
    cols = [0] * W
    total_white = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                rows[i] += 1
                cols[j] += 1
                total_white += 1
    return rows, cols, total_white


solve()
