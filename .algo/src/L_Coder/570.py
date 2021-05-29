# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	// 사용할 배열 초기화
# 	int** arr = (int**)malloc(sizeof(int*) * 5);
# 	int cnt = 0, sum = 0;

# 	for (int i = 0; i < 5; i++)
# 		arr[i] = (int*)malloc(sizeof(int) * 5);

# 	for (int i = 0; i < 5; i++) {
# 		for (int l = 0; l < 5; l++)
# 			arr[i][l] = 1;
# 	}

# 	for (int i = 1; i < 5; i++) {
# 		for (int l = 1; l < 5; l++) {
# 			arr[i][l] = arr[i][l - 1] + arr[i - 1][l];
# 		}
# 	}

# 	// 최종 출력
# 	for (int i = 0; i < 5; i++) {
# 		for (int l = 0; l < 5; l++)
# 			printf("%d ", arr[i][l]);
# 		printf("\n");
# 	}
# 	return 0;
# }