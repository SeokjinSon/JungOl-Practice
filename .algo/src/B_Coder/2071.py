# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	// 사용할 배열 초기화
# 	int n, m;

# 	scanf("%d %d", &n, &m);
# 	int** arr = (int**)malloc(sizeof(int*) * n);
	
# 	for (int i = 0; i < n; i++)
# 		arr[i] = (int*)malloc(sizeof(int) * n);

# 	for (int i = 0; i < n; i++) {
# 		for (int l = 0; l < n; l++)
# 			arr[i][l] = 1;
# 	}

# 	for (int i = 2; i < n; i++) {
# 		for (int l = 1; l < n; l++) {
# 			if (i == l)
# 				break;
# 			else
# 				arr[i][l] = arr[i - 1][l - 1] + arr[i - 1][l];
# 		}
# 	}

# 	switch (m) {
# 	case 1:
# 		for (int i = 0; i < n; i++) {
# 			for (int l = 0; l <= i; l++)
# 				printf("%d ", arr[i][l]);
# 			printf("\n");
# 		}
# 		break;
# 	case 2:
# 		for (int i = 0; i < n; i++) {
# 			for (int l = 0; l < i; l++)
# 				printf(" ");
# 			for (int k = 0; k < n-i; k++)
# 				printf("%d ", arr[n - i - 1][k]);
# 			printf("\n");
# 		}
# 		break;
# 	case 3:
# 		for (int i = n-1; i >=0; i--) {
# 			for (int l = n-1; l >= i; l--)
# 				printf("%d ", arr[l][i]);
# 			printf("\n");
# 		}
# 		break;
# 	}
# 	return 0;
# }