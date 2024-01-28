#include <stdio.h>
#define value 5000

int winorlose(char c, char d) {
  switch (c) {
  case 'A':
    if (d == 'X')
      return 3;
    if (d == 'Y')
      return 4;
    if (d == 'Z')
      return 8;
  case 'B':
    if (d == 'X')
      return 1;
    if (d == 'Y')
      return 5;
    if (d == 'Z')
      return 9;
  case 'C':
    if (d == 'X')
      return 2;
    if (d == 'Y')
      return 6;
    if (d == 'Z')
      return 7;
  }
  return 0;
}
int main() {
  char c[value + 1];
  int netscore = 0;
  for (int i = 0; i < value; i++) {
    scanf(" %c", &c[i]);
    printf("%c\n", c[i]);
  }
  for (int i = 0; i < value / 2; i++) {
    printf("%c, %c\n", c[i], c[i + value / 2]);
    netscore += winorlose(c[i], c[i + value / 2]);
    printf("%d\n", netscore);
  }
  printf("%d\n", netscore);
}
