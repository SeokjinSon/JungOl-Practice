# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int num;
# 	scanf("%d", &num);

# 	for (int i = 1; i <= num * 2 - 1; i++) {
# 		if (i <=num) { // 별 1개부터 출력
# 			for (int l = 0; l < i; l++)
# 				printf("*");
# 			printf("\n");
# 		}
# 		else {
# 			for (int k = 0; k < num * 2 - i; k++)
# 				printf("*");
# 			printf("\n");
# 		}

# 	}
# 	return 0;
# }