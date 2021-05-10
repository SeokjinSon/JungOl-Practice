# C Code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int sum = 0, i = 0;
# 	int num;

# 	while (i <= 19) {
# 		scanf("%d", &num);
# 		if (num == 0) {
# 			printf("%d %d\n", sum, (int)(sum/i));
# 			return;
# 		}
# 		else {
# 			sum += num;
# 			i++;
# 		}
# 	}
# 	printf("%d %d\n", sum, (int)(sum / i));
# 	return 0;
# }