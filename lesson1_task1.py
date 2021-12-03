# вариант 5.	Определить, есть ли среди заданных целых чисел
# A, B, C, D хотя бы одно нечётное.

A = int(input())
B = int(input())
C = int(input())
D = int(input())

A = A % 2
B = B % 2
C = C % 2
D = D % 2

if A == B and B == C and C == D and D == A:
    print("NO")
else:
    print("YES")
