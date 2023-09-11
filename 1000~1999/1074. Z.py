def Z(N, row, column, start):
    if N == 1:
        if row == 0 and column == 0:
            return start
        elif row == 0 and column == 1:
            return start + 1
        elif row == 1 and column == 0:
            return start + 2
        elif row == 1 and column == 1:
            return start + 3
    else:
        # 상단 왼쪽
        if 2**N//2 > row and 2**N//2 > column:
            start = int(2**N * 2**N * (0/4)) + start
            result = Z(N-1, row, column, start)

        # 상단 오른쪽
        elif 2**N//2 > row and 2**N//2 <= column:
            start = int(2**N * 2**N * (1/4)) + start
            result = Z(N-1, row, column-(2**N//2), start)

        # 하단 왼쪽
        elif 2**N//2 <= row and 2**N//2 > column:
            start = int(2**N * 2**N * (2/4)) + start
            result = Z(N-1, row-(2**N//2), column, start)

        # 하단 오른쪽
        elif 2**N//2 <= row and 2**N//2 <= column:
            start = int(2**N * 2**N * (3/4)) + start
            result = Z(N-1, row-(2**N//2), column-(2**N//2), start)
        return result


N, row, column = map(int, input().split())

print(Z(N, row, column, 0))
