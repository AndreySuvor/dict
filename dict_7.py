n = int(input())
d = {}
z = []
for _ in range(n):
    x = (input().split())
    d[x[0]] = x[1:]
dict_spisok = {'write': 'W', 'read': 'R', 'execute': 'X'}
m = int(input())
for _ in range(m):
    y = input().split()
    z.append(y)
result = []
for c in z:
    q = []
    b = dict_spisok[c[0]]
    a = c[1]
    for key, value in d.items():
        if key == a and b in value:
            print('OK')
            break
    else:
        print('Access denied')