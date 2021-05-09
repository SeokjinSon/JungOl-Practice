# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n, sum = 0, cnt = 0;
# 	scanf("%d", &n);

# 	for (int i = n; i > 0; i--) {
# 		for (int l = 0; l < n - i; l++)
# 			printf(" ");
# 		for (int j = 0; j < i * 2 - 1; j++)
# 			printf("*");
# 		for (int k = 0; k < n - i; k++)
# 			printf(" ");
# 		printf("\n");
# 	}

# 	return 0;
# }