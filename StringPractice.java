import java.util.*;

public class StringPractice {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    
    System.out.println("What is your name? ");
    String a = scan.nextLine();
    
    int b = a.length();
    char c = a.charAt(1);
    
    System.out.println("There are " + b + " letters in your name and the 2nd letter is " + c);
    
  }
}
