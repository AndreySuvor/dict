s = input().lower().split()
result = {}
lst = []
x = '.,!?:;'
for c in s:
    if c[-1] in x:
        c = c[:-1]
    elif '-' in c:
        c = c.replace('-', '')
    result[c] = result.get(c, 0) + 1
m = min(result.values())
for key, value in result.items():
    if value == m:
        lst.append(key)
print(min(lst))

