
'''
def transform(input_str:str):
    new_str = ""
    input_str = input_str.lower()
    for char in input_str:
        if char == 'z':
            new_str = new_str + 'ab'
            continue
        ascii_val = ord(char)
        new_ascii = ascii_val + 1
        new_char = chr(new_ascii)
        new_str = new_str + new_char
    return new_str

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    trans = int(input("enter number of transformations: "))
    for i in range(trans):
        input_str = transform(input_str)
        print(input_str)
    print(len(input_str))
'''

from collections import deque

r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]

rotten_q = deque()
fresh_c = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 2:
            rotten_q.append((i, j))
        elif matrix[i][j] == 1:
            fresh_c += 1

minutes = 0
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while rotten_q and fresh_c > 0:
    for _ in range(len(rotten_q)):
        x, y = rotten_q.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] == 1:
                matrix[nx][ny] = 2
                rotten_q.append((nx, ny))
                fresh_c -= 1
    minutes += 1

print(minutes if fresh_c == 0 else -1)









