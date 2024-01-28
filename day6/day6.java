import java.util.*;

class day6 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    int n = 4;
    // System.out.println("Enter n");
    // int n = sc.nextInt();
    System.out.println(checker(s, n));
    sc.close();
  }

  static int checker(String s, int n) {
    for (int i = 0; i < s.length(); i++)
      if (!repeat(s.substring(i, i + n)))
        return i;
    return 0;
  }

  static boolean repeat(String s) {
    for (int i = 0; i < s.length(); i++) {
      for (int j = i; j < 0; j++)
        if (s.charAt(i) == s.charAt(j))
          return false;
    }
    return true;
  }
}
