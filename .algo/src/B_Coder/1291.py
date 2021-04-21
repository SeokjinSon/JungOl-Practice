
# 값 입력
def calculate(i, l):
    result = '%2s' % '{}'.format(i*l)
    print("{} * {} = {}".format(int(l), int(i), result), end="   ")

while True:
    s, e = map(int, input().split())
    if (s<2 or s>9) or (e<2 or e>9):
        print("INPUT ERROR!")
    else:
        break;

if s<e:
    for i in range(1, 9+1, 1):
        for l in range(s, e+1, 1):
            calculate(i, l)
        print()
else:
    for i in range(1, 9+1, 1):
        for l in range(s, e-1, -1):
            calculate(i, l)
        print()