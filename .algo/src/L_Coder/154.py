# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	double arr[6] = { 0, };
# 	double sum = 0;

# 	for (int i = 0; i < 6; i++) {
# 		scanf("%lf", &arr[i]);
# 		sum += arr[i];
# 	}

# 	printf("%0.1f\n", sum / 6);


# 	return 0;
# }