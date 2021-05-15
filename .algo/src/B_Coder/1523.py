# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main(void) {
# 	int n, m, cnt; // 높이, 종류
# 	scanf("%d %d", &n, &m);

# 	if (n<1 || n > 100 || m < 1 || m>3) {
# 		printf("INPUT ERROR!\n");
# 		return;
# 	}

# 	switch (m) {
# 	case 1:
# 		for (int i = 1; i <= n; i++) {
# 			for (int l = 1; l <= i; l++)
# 				printf("*");
# 			printf("\n");
# 		}
# 		break;
# 	case 2:
# 		for (int i = n; i >= 1; i--) {
# 			for (int l = 1; l <= i; l++)
# 				printf("*");
# 			printf("\n");
# 		}
# 		break;
# 	case 3:
# 		for (int i = 1; i <= n; i++) {
# 			for (int l = 0; l < n - i; l++)
# 				printf(" ");
# 			for (int k = 0; k < i * 2 - 1; k++)
# 				printf("*");
# 			printf("\n");
# 		}
# 		break;
# 	}

# 	return 0;
# }