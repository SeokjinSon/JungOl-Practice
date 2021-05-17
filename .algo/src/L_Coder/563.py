# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int arr[10] = { 0, };
# 	int max = 0;

# 	for (int i = 0; i < 10; i++)
# 		scanf("%d", &arr[i]);

# 	for (int i = 0; i < 10; i++) {
# 		for (int l = i; l < 10; l++) {
# 			if (arr[i] < arr[l]) {
# 				int swp = arr[i];
# 				arr[i] = arr[l];
# 				arr[l] = swp;
# 			}
# 		}
# 	}

# 	for (int i = 0; i < 10; i++)
# 		printf("%d ", arr[i]);

# 	return 0;
# }