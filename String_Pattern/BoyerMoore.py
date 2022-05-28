t = input()
p = input()

def boyer_moore(t, p):
     n = len(t)
     m = len(p)
     index = 0
     while index <= n - m:
         j = m - 1
         while j >= 0:
             if p[j] != t[i+j]:
                 move = skip(p, t[index + m - 1])
                 break
             j -= 1
         if j == -1:
             return True
         else:
             index += move
     return False

def skip(p, c):
    for i in range(len(p)-2, -1, -1):
        if p[i] == c:
            return len(p) - 1 - i
    return len(p)

print(boyer_moore(t, p))