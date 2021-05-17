# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n, m, mid; // n : 삼각형 크기, m : 종류
# 	scanf("%d %d", &n, &m);
# 	mid = n / 2 + 1;

# 	if (n > 100 || n % 2 == 0 || m < 1 || m>4) {
# 		printf("INPUT ERROR!\n");
# 		return;
# 	}

# 	switch (m) {
# 	case 1:
# 		for (int i = 0; i < n; i++) {
# 			if (i < mid) {
# 				for (int l = 0; l <= i; l++)
# 					printf("*");
# 				printf("\n");
# 			}
# 			else {
# 				for (int l = 0; l < n - i; l++)
# 					printf("*");
# 				printf("\n");
# 			}
# 		}
# 		break;
# 	case 2:
# 		for (int i = 0; i < n; i++) {
# 			if (i < mid) {
# 				for (int k = 1; k < mid - i; k++)
# 					printf(" ");
# 				for (int l = 0; l <= i; l++)
# 					printf("*");
# 				printf("\n");
# 			}
# 			else {
# 				for (int k = 0; k <= i - mid; k++)
# 					printf(" ");
# 				for (int l = 0; l < n - i; l++)
# 					printf("*");
# 				printf("\n");
# 			}
# 		}
# 		break;
# 	case 3:
# 		for (int i = 1; i <= n; i++) {
# 			if (i <= mid) {
# 				for (int k = 1; k < i; k++)
# 					printf(" ");
# 				for (int l = mid * 2 - i * 2; l >= 0; l--)
# 					printf("*");
# 				for (int k = 1; k < i; k++)
# 					printf(" ");
# 				printf("\n");
# 			}
# 			else {
# 				for (int k = 0; k < n - i; k++)
# 					printf(" ");
# 				for (int l = i * 2 - mid * 2; l >= 0; l--)
# 					printf("*");
# 				for (int k = 0; k < n - i; k++)
# 					printf(" ");
# 				printf("\n");
# 			}
# 		}
# 		break;
# 	case 4:
# 		for (int i = 0; i < n; i++) {
# 			if (i < mid) {
# 				for (int l = 0; l < i; l++)
# 					printf(" ");
# 				for (int l = 0; l < mid - i; l++)
# 					printf("*");
# 				printf("\n");
# 			}
# 			else {
# 				for (int k = 1; k < mid; k++)
# 					printf(" ");
# 				for (int k = 0; k <= i - mid + 1; k++)
# 					printf("*");
# 				printf("\n");
# 			}
# 		}
# 		break;
# 	}
# 	return 0;
# }