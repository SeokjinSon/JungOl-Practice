# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int arr[10];
# 	int c1 = 0, c2 = 0;

# 	for (int i = 0; i < 10; i++) {
# 		scanf("%d", &arr[i]);
# 		if (arr[i] % 3 == 0)
# 			c1++;
# 		if (arr[i] % 5 == 0)
# 			c2++;
# 	}

# 	printf("Multiples of 3 : %d\n", c1);
# 	printf("Multiples of 5 : %d\n", c2);
# 	return 0;
# }