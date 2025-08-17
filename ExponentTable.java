import java.util.*;

public class ExponentTable {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    
    System.out.println("Enter a cut off number: ");
    int a = scan.nextInt();
    
    
    System.out.println(" x \t x^2 \t x^3");
    for(int x = 1; x <=a; x++){
        System.out.println(x + "\t" + (int)Math.pow(x, 2) + "\t" + (int)Math.pow(x,3));
    }
    
  }
}
