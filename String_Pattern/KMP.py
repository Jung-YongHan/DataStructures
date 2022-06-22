def compute_lps(p, lps):
    length = 0
    i = 1  # lps[0]은 prefix, suffix가 존재 x -> 1부터 시작
    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def kmp(t, p):
    n = len(t)
    m = len(p)
    result = []

    lps = [0] * (m + 1)
    compute_lps(p, lps)

    i = j = 0  # i는 text 인덱스, j는 패턴 인덱스
    while i < n:
        if t[i] == p[j]:
            i += 1
            j += 1
            if j == m:
                result.append(i - j + 1)
                j = lps[j-1]
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
    return result

t = input()
p = input()
print(*kmp(t, p))