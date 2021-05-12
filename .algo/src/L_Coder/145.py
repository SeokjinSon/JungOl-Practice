# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() { // 별 개수 및 반복 횟수 : 2n-1
# 	int n;
# 	scanf("%d", &n);

# 	for (int i = 0; i < n; i++) {
# 		for (int k = 1; k < n-i; k++)
# 			printf("  ");
# 		for (int l = 0; l <= i; l++)
# 			printf("%d ", l+1);
# 		printf("\n");
# 	}
# 	return 0;
# }