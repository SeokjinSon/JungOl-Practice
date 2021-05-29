# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	// 사용할 배열 초기화
# 	int** arr1 = (int**)malloc(sizeof(int*) * 2);
# 	int** arr2 = (int**)malloc(sizeof(int*) * 2);

# 	for (int i = 0; i < 2; i++)
# 		arr1[i] = (int*)malloc(sizeof(int) * 4);
# 	for (int i = 0; i < 2; i++)
# 		arr2[i] = (int*)malloc(sizeof(int) * 4);

# 	printf("first array\n");
# 	for (int i = 0; i < 2; i++) {
# 		for (int l = 0; l < 4; l++)
# 			scanf("%d", &arr1[i][l]);
# 	}
# 	printf("second array\n");
# 	for (int i = 0; i < 2; i++) {
# 		for (int l = 0; l < 4; l++)
# 			scanf("%d", &arr2[i][l]);
# 	}

# 	// 최종 출력
# 	for (int i = 0; i < 2; i++) {
# 		for (int l = 0; l < 4; l++) {
# 			printf("%d ", arr1[i][l] * arr2[i][l]);
# 		}
# 		printf("\n");
# 	}
	
# 	return 0;
# }