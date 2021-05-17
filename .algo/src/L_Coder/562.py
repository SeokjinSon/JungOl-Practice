# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int arr[10] = { 0, };
# 	int sum1 = 0, sum2 = 0;

# 	for (int i = 0; i < 10; i++) {
# 		scanf("%d", &arr[i]);
# 		if (i % 2 == 0)
# 			sum2 += arr[i];
# 		else
# 			sum1 += arr[i];
# 	}

# 	printf("sum : %d\n", sum1);
# 	printf("avg : %0.1f\n", (double)sum2 / 5);

# 	return 0;
# }