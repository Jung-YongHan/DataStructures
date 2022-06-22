t=input()
p=input()

def br(t, p):
    i = j = 0
    while i < len(t) and j < len(p):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        return i-j
    else:
        return -1

print(br(t, p))