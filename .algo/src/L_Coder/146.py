# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n, ch=65, num=0;
# 	scanf("%d", &n);

# 	for (int i = 0; i < n; i++) {
# 		for (int l = n - i; l > 0; l--)
# 			printf("%c ", ch++);
# 		for (int k = 0; k < i; k++)
# 			printf("%d ", num++);
# 		printf("\n");
# 	}

# 	return 0;
# }