# C code
# 약수 : 어떤 수를 나누어 떨어지게 하는 수를 그 수의 약수라 한다.
# 배수 : 어떤 수를 1배, 2배 ... 한 수를 그 수의 배수라 한다.

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n, m;
# 	int div = 0, mul = 0;
# 	int* arr;

# 	scanf("%d", &n);
# 	arr = (int)malloc(sizeof(int) * n);
# 	for (int i = 0; i < n; i++)
# 		scanf("%d", &arr[i]);
# 	scanf("%d", &m);

# 	for (int i = 0; i < n; i++) {
# 		if (arr[i] > m) { // 배수 구하기
# 			if (arr[i] % m == 0)
# 				mul+=arr[i];
# 		}
# 		else if (arr[i] < m) { // 약수 구하기
# 			if (m % arr[i] == 0)
# 				div+=arr[i];
# 		}
# 		else { // 동일한 수(약수이면서 배수)
# 			div += arr[i];
# 			mul += arr[i];
# 		}
# 	}

# 	printf("%d\n", div);
# 	printf("%d\n", mul);

# 	return 0;
# }