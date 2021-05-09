# C Code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n, sum = 0, cnt = 0;
# 	scanf("%d", &n);

# 	for (int i = n; i >= 1; i--) {
# 		for (int l = 0; l < i; l++)
# 			printf("*");
# 		printf("\n");
# 	}

# 	for (int i = 1; i <= n; i++) {
# 		for (int l = 0; l < i; l++)
# 			printf("*");
# 		printf("\n");
# 	}

# 	return 0;
# }