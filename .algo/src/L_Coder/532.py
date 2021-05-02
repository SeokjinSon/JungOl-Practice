num1, num2 = input().split()

num1 = float(num1)
num2 = float(num2)

if num1>=4.0 and num2>=4.0:
    print("A")
elif num1>=3.0 and num2>=3.0:
    print("B")
else:
    print("C")