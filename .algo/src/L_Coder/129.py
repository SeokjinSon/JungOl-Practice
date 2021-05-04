while(1):
    b = input("Base = ")
    h = input("Height = ")
    print("Triangle width = {}".format(round(float(int(b)*int(h)/2), 1)))
    c = input("Continue? ").strip()

    if(c == 'Y' or c == 'y'):
        continue
    else:
        break
    
