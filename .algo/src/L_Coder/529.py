height, weight = input().split()
obesity = int(weight)+100-int(height)

print(obesity)
if(obesity>0):
    print("Obesity")