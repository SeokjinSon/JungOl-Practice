# C code

# int main() { // 별 개수 및 반복 횟수 : 2n-1
# 	int n, m;
# 	scanf("%d", &n);
# 	m = n+1;
	
# 	for (int i = 1; i <= n * 2 - 1; i++) {
# 		if (i <= n) {
# 			m--;
# 			for (int j = 1; j < i; j++)
# 				printf(" ");
# 			for (int l = 1; l <= m * 2 - 1; l++)
# 				printf("*");
# 			printf("\n");
# 		}
# 		else {
# 			m++;
# 			for (int j = 1; j < n * 2 - i; j++)
# 				printf(" ");
# 			for (int k = 1; k <= m * 2 - 1; k++)
# 				printf("*");
# 			printf("\n");
# 		}
# 	}

# 	return 0;
# }
