# 2개의 실수 입력
n1, n2 = input().split()

# 입력한 2개의 실수를 곱한 후 정수형으로 변환
r1 = int(float(n1)*float(n2))

# 입력한 2개의 실수를 각각 정수형으로 변환 후 곱하기
r2 = int(float(n1))*int(float(n2))

# 결과값 출력
print("{} {}".format(r1, r2))