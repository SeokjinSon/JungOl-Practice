# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main(void) {
# 	int value, n1=0, n2=9999;
	

# 	for (int i = 0; i < 10; i++) {
# 		scanf("%d", &value);
# 		if (value < 100 && value > n1)
# 			n1 = value;
# 		else if (value >= 100 && value <= n2)
# 			n2 = value;
# 	}

# 	if (n1 == 0)
# 		printf("100 ");
# 	else
# 		printf("%d ", n1);

# 	if (n2 == 9999)
# 		printf("100");
# 	else
# 		printf("%d", n2);

# 	return 0;
# }