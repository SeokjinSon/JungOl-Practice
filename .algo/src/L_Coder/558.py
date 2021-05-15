# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main(void) {
# 	int arr[100] = { 0, };
# 	int i = 0;


# 	do {
# 		scanf("%d", &arr[i]);
# 	} while (arr[i++] != 0);

# 	i-=2;
# 	for (int l = i; l >= 0; l--)
# 		printf("%d ", arr[l]);

# 	return 0;
# }