# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() { 
# 	int n, num=1;
# 	scanf("%d", &n);

# 	for (int i = 0; i < n; i++) {
# 		for (int l = 0; l < i; l++)
# 			printf("  ");
# 		for (int k = 0; k < n - i; k++)
# 			printf("%d ", num++);
# 		printf("\n");
# 	}
# 	return 0;
# }