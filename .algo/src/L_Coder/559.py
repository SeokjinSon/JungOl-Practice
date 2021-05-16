# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main(void) {
# 	double arr[6];
# 	int n1, n2;
# 	double sum = 0;

# 	arr[0] = 85.6;
# 	arr[1] = 79.5;
# 	arr[2] = 83.1;
# 	arr[3] = 80.0;
# 	arr[4] = 78.2;
# 	arr[5] = 75.0;

# 	scanf("%d %d", &n1, &n2);

# 	for (int i = 1; i <= 6; i++) {
# 		if (i == n1 || i == n2)
# 			sum += arr[i-1];
# 	}

# 	printf("%0.1f\n", sum);
		
# 	return 0;
# }