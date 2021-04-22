hn, wm = map(int, input().split())

for i in range(1, hn*wm+1, 1):
    print(i, end=" ")

    if(i%wm==0):
        print()