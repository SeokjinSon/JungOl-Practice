# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() { 
# 	int n, cnt = 1;
# 	scanf("%d", &n);

# 	for (int i = 0; i < n; i++) {
# 		for (int l = 0; l < n; l++) {
# 			if (cnt > 10)
# 				cnt = 1;
# 			printf("%d ", cnt);
# 			cnt += 2;
# 		}
# 		printf("\n");
# 	}
# 	return 0;
# }