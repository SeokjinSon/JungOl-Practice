# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int cnt = 0;
# 	int arr[100] = { 0, };

# 	for (int i = 0; i < 100; i++) {
# 		scanf("%d", &arr[i]);
# 		if (arr[cnt] == 0) {
# 			printf("%d\n", cnt);
# 			for (int l = 0; l < cnt; l++) {
# 				if (arr[l] % 2 != 0)
# 					printf("%d ", arr[l] * 2);
# 				else
# 					printf("%d ", arr[l] / 2);
# 			}
# 			break;
# 		}
# 		cnt++;
# 	}

# 	return 0;
# }