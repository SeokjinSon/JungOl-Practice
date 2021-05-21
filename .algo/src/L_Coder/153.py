# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int arr[100] = { 0, };
# 	int cnt = 0;

# 	while (1) {
# 		scanf("%d", &arr[cnt++]);
# 		if (arr[cnt-1] == -1) {
# 			if (cnt <= 3) {
# 				for (int i = 0; i < cnt-1; i++)
# 					printf("%d ", arr[i]);
# 			}
# 			else {
# 				printf("%d %d %d\n", arr[cnt- 4], arr[cnt - 3], arr[cnt - 2]);
# 			}
# 			break;
# 		}
# 	}

# 	return 0;
# }