import sys

if __name__ == '__main__':
    n = int(input())
    board = []
    found = []
    valid = True
    for i in range(0,n):
        line = input().split()
        row = []
        for x in line:
            if int(x) in found:
                print("Invalid data: missing or repeated number")
                exit()
            found.append(int(x))
            row.append(int(x))
        if len(row) < n:
            print("Invalid data: missing or repeated number")
            exit()
        board.append(row)
    target = sum(board[0])
    for x in board:
        if sum(x)!=target:
            valid = False
            break
        diagTotal = 0
        for i in range(0, n):
            diagTotal += board[i][i]
            total = 0
            for j in range(0, n):
                total += board[i][j]
            if total!=target:
                valid = False
                break
        if diagTotal!=target:
            valid = False
            break
    if valid:
        print("Magic Square")
    else:
        print("Invalid data: inconsistent sums")