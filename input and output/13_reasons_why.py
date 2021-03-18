A, B, C = map(int, input().split())
A, B = B, A
A *= C
B += C
print(A,B)
