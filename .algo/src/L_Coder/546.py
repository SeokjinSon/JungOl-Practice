# C code

# #define _CRT_SECURE_NO_WARNINGS
# #include <stdio.h>
# #include <stdlib.h>
# #include <math.h> //C언어

# int main() {
# 	int num, sum=0;
# 	double avg = 0;
# 	int* arr;
# 	scanf("%d", &num);
# 	arr = (int)malloc(sizeof(int) * num);

# 	for (int i = 0; i < num; i++) {
# 		int value;
# 		scanf("%d", &value);
# 		arr[i] = value;
# 	}

# 	for (int i = 0; i < num; i++)
# 		sum += arr[i];

# 	avg = (double)sum / num;

# 	printf("avg : %0.1f\n", avg);
# 	if (avg >= 80)
# 		printf("pass\n");
# 	else
# 		printf("fail\n");

		


# 	return 0;
# }