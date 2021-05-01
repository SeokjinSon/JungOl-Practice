# 2개의 정수 입력
n1, n2 = input().split()

# 첫 번째 수를 두 번째 수로 나눈 몫 출력
r1 = int(n1)/int(n2)

# 소수 둘째 자리까지 출력하는 프로그램
r2 = round(float(n1)/float(n2), 2)

# 결과 출력
print("{} {}".format(int(r1), r2))