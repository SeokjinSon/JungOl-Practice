# 인자 입력
s, e = map(int, input().split())

def calculate(i):
    k=0
    for l in range(1, 9+1, 1):
        if(k==3):
            k=0
            print()

        result = '%2s' % '{}'.format(i*l)
        print("{} * {} = {}".format(i, l, result), end="   ")
        k+=1
    print()
    print()

# 조건에 따른 출력
if s<e:
    for i in range(s, e+1, 1):
        calculate(i)

else:
    for i in range(s, e-1, -1):
        calculate(i)