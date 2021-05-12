# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() { // 별 개수 및 반복 횟수 : 2n-1
# 	int n;
# 	scanf("%d", &n);

# 	for (int i = 0; i < n; i++) {
# 		for (int k = 1; k <= (n * 2 - 1) - (i * 2 + 1); k++)
# 			printf(" ");
# 		for (int l = 1; l <= i*2+1; l++)
# 			printf("%d ", l);
# 		printf("\n");
# 	}
# 	return 0;
# }