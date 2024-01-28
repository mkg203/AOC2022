#include <stdio.h>
#define value 5000

int winorlose(char c, char d) {
  if (c == 'A' && d == 'X' || c == 'B' && d == 'Y' || c == 'C' && d == 'Z')
    return (d == 'X') ? 4 : (d == 'Y') ? 5 : 6;
  return (c == 'A') ? (d == 'Y') ? 8 : 3 // if c = rock and d = paper, return 2
                                         // + 6, if d = scissors return 3 + 0
         : (c == 'B')
             ? (d == 'Z') ? 9 : 1 // if c = paper and d = scissors, return 3 +
                                  // 6, if d = rock return 1 + 0
         : (c == 'C')
             ? (d == 'X') ? 7 : 2 // if c = scissors and d = rock, return 1 + 6,
                                  // if d = paper return 2 + 0
             : 0;
}
int main() {
  char c[value + 1];
  int netscore = 0;
  for (int i = 0; i < value; i++) {
    // c[i] = getchar();
    scanf(" %c", &c[i]);
    printf("%c\n", c[i]);
  }
  for (int i = 0; i < value / 2; i++) {
    printf("%c, %c\n", c[i], c[i + value / 2]);
    netscore += winorlose(c[i], c[i + value / 2]);
  }
  printf("%d\n", netscore);
}
