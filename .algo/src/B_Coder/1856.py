n1, n2 = map(int, input().split())

k=0;
for i in range(1, n1+1, 1):
    if(i%2==1):
        for l in range(k+1, k+n2+1, 1):
            k+=1
            print(l, end = " ")
    else:
        for l in range(k+n2, k, -1):
            k+=1
            print(l, end = " ")
    print()