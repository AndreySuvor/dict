s = input().split()
result = {}
for c in s:
    result[c] = result.get(c, - 1) + 1
    if result[c] == 0:
        print(c, end=' ')
    else:
        print(c + '_' + str(result[c]), end=' ')