# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int n1, n2, n3, result=0, value=0;
# 	int arr[10] = { 0, };
# 	scanf("%d %d %d", &n1, &n2, &n3);

# 	result = n1 * n2 * n3;

# 	while (result >= 10) {
# 		value = result % 10;
# 		arr[value]++;
# 		result /= 10;
# 	}
# 	arr[result]++;

# 	for (int i = 0; i < sizeof(arr) / sizeof(int); i++)
# 		printf("%d\n", arr[i]);

# 	return 0;
# }