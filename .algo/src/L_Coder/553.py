# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n, num=65;
# 	scanf("%d", &n);

# 	for (int i = 0; i < n; i++) {
# 		for (int l = 0; l < n - i; l++)
# 			printf("%c", num++);
# 		printf("\n");
# 	}

# 	return 0;
# }