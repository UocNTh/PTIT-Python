import os
os.system('cls')
n = int(input())
a = [''] * n

for i in range(n) :
    a[i] = input()

s = a[0]
m, kt, ans = len(s), 1, 10**9
for i in range(m) :
    d = 0
    for j in range(n) :
        x = a[j]
        for k in range(m) :
            if x == s :
                d += k
                break
            x = x[1::] + x[0]
        if x != s : kt = 0
    ans = min(ans, d)
    s = s[1::] + s[0]
if kt == 0 : print(-1)
else : print(ans)