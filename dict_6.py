d = {}
for i in range(int(input())):
    a, b, c = input().split()
    d[a] = d.get(a, {})
    d[a][b] = d.get(a, {}).get(b, 0) + int(c)
for i in sorted(d):
    print(f'{i}:', sep='\n')
    for k in sorted(d[i]):
        print(f'{k} {d[i][k]}', sep='\n')