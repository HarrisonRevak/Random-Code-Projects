import java.util.*;

public class JavaCalc {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    
    double a = Math.random()*99+1;
    int b = (int)a;
    
    System.out.println(b + "is your random number");
    
    System.out.println("Enter a number to square root! ");
    int c = scan.nextInt();
    
    System.out.println(Math.sqrt(c));
    
    System.out.println("Enter a number to square");
    int d = scan.nextInt();
    
    System.out.println(Math.pow(d,2));
    
    System.out.println("Enter a number to cube");
    int e = scan.nextInt();
    
    System.out.println(Math.pow(e,3));
    
  }
}
