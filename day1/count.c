#include <stdio.h>
int main() {
  int max = 0, max2 = 0, max3 = 0, sum = 0, input;
  while (input != 1) {
    scanf("%d", &input);
    if (input == 0) {
      if (max < sum) {
        max3 = max2;
        max2 = max;
        max = sum;
      } else if (max2 < sum) {
        max3 = max2;
        max2 = sum;
      } else if (max3 < sum)
        max3 = sum;
      sum = 0;
    }
    sum += input;
  }
  printf("%d, %d, %d\n", max, max2, max3);
  printf("%d\n", max + max2 + max3);
}
