# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n, ch=65, num=1;
# 	scanf("%d", &n);

# 	for (int i = n; i >= 1; i--) {
# 		for (int l = 0; l < i; l++)
# 			printf("%d ", num++);
# 		for (int k = 0; k <= n - i; k++)
# 			printf("%c ", ch++);
# 		printf("\n");
# 	}

# 	return 0;
# }