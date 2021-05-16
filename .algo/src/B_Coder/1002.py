# C code
# gcd, lcm 따로 구하도록 해서 만듦

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
# #include <stdlib.h>

# int getGcd(int v1, int v2);
# int getLcm(int v1, int v2);

# int main() {
# 	int n1, n2, N;
# 	int* arr;
# 	int gcd = 1;
# 	int lcm = 1;

# 	scanf("%d", &N);
# 	arr = (int)malloc(sizeof(int) * N);

# 	for (int i = 0; i < N; i++)
# 		scanf("%d", &arr[i]);

# 	gcd = getGcd(arr[0], arr[1]);
# 	lcm = getLcm(arr[0], arr[1]);

# 	for (int i = 2; i < N; i++) {
# 		gcd = getGcd(gcd, arr[i]);
# 		lcm = getLcm(lcm, arr[i]);
# 	}

# 	printf("%d %d", gcd, lcm);

# 	return 0;
# }

# // 두 수의 최소공배수 및 최대공약수 출력
# int getGcd(int v1, int v2) {
# 	int min, n1, n2, gcd;
# 	n1 = v1;
# 	n2 = v2;
# 	gcd = 1;

# 	if (n1 < n2)
# 		min = n1;
# 	else
# 		min = n2;

# 	while (1) {
# 		for (int i = 2; i <= min; i++) {
# 			if (n1 % i == 0 && n2 % i == 0) { // 나누어 떨어짐
# 				gcd *= i;
# 				n1 /= i;
# 				n2 /= i;
# 				break;
# 			}
# 			else {
# 				if (i == min)
# 					return gcd;
# 			}
# 		}
# 	}
# }

# int getLcm(int v1, int v2) {
# 	int min, n1, n2, lcm;
# 	n1 = v1;
# 	n2 = v2;
# 	lcm = 1;

# 	if (n1 < n2)
# 		min = n1;
# 	else
# 		min = n2;

# 	while (1) {
# 		for (int i = 2; i <= min; i++) {
# 			if (n1 % i == 0 && n2 % i == 0) { // 나누어 떨어짐
# 				lcm *= i;
# 				n1 /= i;
# 				n2 /= i;
# 				break;
# 			}
# 			else {
# 				if (i == min)
# 					return (lcm * n1 * n2);
# 			}
# 		}
# 	}
# }
