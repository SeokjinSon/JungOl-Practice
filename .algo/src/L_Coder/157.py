# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>

# int main() {
# 	int val = 0, cnt = -1, sum = 0;

# 	do {
# 		scanf("%d", &val);

# 		if (val%5==0) {
# 			sum += val;
# 			cnt++;
# 		}
# 	} while (val != 0);

# 	printf("Multiples of 5 : %d\n", cnt);
# 	printf("sum : %d\n", sum);
# 	printf("avg : %0.1f\n", sum / (double)cnt);

# 	return 0;
# }