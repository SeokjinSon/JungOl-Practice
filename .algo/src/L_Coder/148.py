# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() { 
# 	int n, cnt;
# 	scanf("%d", &n);

# 	cnt = n * 2 - 1;

# 	for (int i = 1; i <= cnt; i++) {
# 		if (i <= n) {
# 			for (int l = 0; l < i; l++)
# 				printf("# ");
# 			printf("\n");
# 		}
# 		else {
# 			for (int k = 0; k < i-n; k++)
# 				printf("  ");
# 			for (int j = 0; j < n-(i-n); j++)
# 				printf("# ");
				
# 			printf("\n");
# 		}
# 	}
# 	return 0;
# }