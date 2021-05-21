# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n, m, mid, cnt = 1, swp;
# 	scanf("%d %d", &n, &m);
# 	mid = n / 2;

# 	if (n > 100 || n % 2 == 0 || m < 1 || m>3) {
# 		printf("INPUT ERROR!\n");
# 		return;
# 	}

# 	switch (m) {
# 	case 1:
# 		for (int i = 1; i <= n; i++) {
# 			if (i % 2 != 0) { // 홀수 번쨰
# 				swp = cnt;
# 				for (int l = swp; l < swp + i; l++) {
# 					printf("%d ", l);
# 					cnt++;
# 				}
# 				printf("\n");
# 			}
# 			else { // 짝수 번째
# 				swp = cnt;
# 				for (int l = swp + i - 1; l >= swp; l--) {
# 					printf("%d ", l);
# 					cnt++;
# 				}
# 				printf("\n");					
# 			}
# 		}
# 		break;
# 	case 2:
# 		for (int i = 0; i < n; i++) {
# 			for (int l = 0; l < i; l++)
# 				printf("  ");
# 			for (int k = 0; k < n * 2 - 1 - i * 2; k++)
# 				printf("%d ", i);
# 			printf("\n");
# 		}
# 		break;
# 	case 3:
# 		for (int i = 0; i < n; i++) {
# 			if (i <=mid) {
# 				for (int l = 0; l <= i; l++)
# 					printf("%d ", l + 1);
# 				printf("\n");
# 			}
# 			else {
# 				for (int k = 0; k < n-i; k++)
# 					printf("%d ", k+1);
# 				printf("\n");
# 			}
# 		}
# 		break;
# 	}

# 	return 0;
# }