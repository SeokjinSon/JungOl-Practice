# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main(void) {
# 	int value, min = 1001;


# 	for (int i = 0; i < 10; i++) {
# 		scanf("%d", &value);
# 		if (min > value)
# 			min = value;
# 	}

# 	printf("%d\n", min);
		
# 	return 0;
# }