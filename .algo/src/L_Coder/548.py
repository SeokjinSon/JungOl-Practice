for i in range(2, 4+1):
    for l in range(1, 5+1):
        print(str(i) + " * " + str(l) + " = " + str(i*l).rjust(2), end='   ')
    print()