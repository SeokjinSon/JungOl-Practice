# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int max = -1000, min = 1000;
# 	int val = 0;

# 	while (1) {
# 		scanf("%d", &val);

# 		if (val == 999)
# 			break;

# 		if (min > val)
# 			min = val;
# 		else if (max < val)
# 			max = val;
# 	}

# 	printf("max : %d\n", max);
# 	printf("min : %d\n", min);

# 	return 0;
# }