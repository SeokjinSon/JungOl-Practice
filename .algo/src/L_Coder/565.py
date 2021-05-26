# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int arr[10] = { 0, };
# 	int input;

# 	while (1) {
# 		scanf("%d", &input);

# 		if (input != 0)
# 			arr[input / 10]++;
# 		else
# 			break;
# 	}

# 	for (int i = 0; i < 10; i++) {
# 		if (arr[i] != 0)
# 			printf("%d : %d\n", i, arr[i]);
# 	}
	
# 	return 0;
# }