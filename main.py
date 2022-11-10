def s(x):
    print('here')
    if x == 0:
        return 0
    else:
        sum = s(x-1)
        return x + sum

def recur(x):
    if x == 0:
        return 0
    else:
        return x + recur(x-1)
print(recur(5))