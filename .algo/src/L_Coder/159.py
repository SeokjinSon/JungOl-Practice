# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int cnt = 0;
# 	int* arr;

# 	scanf("%d", &cnt);
# 	arr = (int)malloc(sizeof(int) * cnt);

# 	for (int i = 0; i < cnt; i++)
# 		scanf("%d", &arr[i]);

# 	for (int i = 0; i < cnt; i++) {
# 		for (int l = 0; l < cnt; l++) {
# 			if (arr[i] < arr[l]) {
# 				int swp = arr[i];
# 				arr[i] = arr[l];
# 				arr[l] = swp;
# 			}
# 		}
# 	}

# 	for (int i = cnt - 1; i >= 0; i--)
# 		printf("%d\n", arr[i]);

# 	return 0;
# }