# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
# #include <math.h>

# int main() { // 별 개수 및 반복 횟수 : 2n-1
# 	int n, num, cnt=0;
# 	int arr[10000] = { 0, };
# 	scanf("%d", &n);
# 	num = (int)(sqrt(n));

# 	for (int i = 1; i <= num; i++) {
# 		if (n % i == 0) {
# 			arr[cnt++] = i;
# 			if (n / i != i)
# 				arr[cnt++] = n / i;
# 		}
# 	}

# 	for (int i = 0; i < cnt; i += 2)
# 		printf("%d ", arr[i]);
# 	if (cnt % 2 == 0) { // 짝수일 경우
# 		for (int i = cnt-1; i >= 1; i -= 2)
# 			printf("%d ", arr[i]);
# 	}
# 	else {
# 		for (int i = cnt - 2; i >= 1; i -= 2)
# 			printf("%d ", arr[i]);
# 	}
	
# 	return 0;
# }