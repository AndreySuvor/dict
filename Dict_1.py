d = {}
for _ in range(int(input())):
    x = input().upper().split()
    if x[1] in d:
        d[x[1]] += ' ' + x[0]
    else:
        d[x[1]] = x[0]
for _ in range(int(input())):
    name = input().upper()
    result = d.get(name, "абонент не найден")
    print(result)