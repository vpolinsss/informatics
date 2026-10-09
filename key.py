n = int(input())
a = []
d = 2
while d*d <= n:
    if n%d == 0:
        a.append(d)
        n = n//d

    else:
        d += 1

if n>1:
    a.append(n)

print(a)

