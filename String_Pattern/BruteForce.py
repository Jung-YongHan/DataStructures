# 입력 문자열에서 패턴을 찾는 알고리즘
t = input()
p = input()
n = len(t)
m = len(p)

def bruteforce(t, p):
    i = j = 0
    while i < n and j < m:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == m:
        return i - m
    else:
        return -1

print(bruteforce(t, p))