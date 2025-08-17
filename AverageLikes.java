import java.util.*;

public class AverageLikes {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    
    System.out.println("How many likes did your most recent post get? ");
    int a = scan.nextInt();
    
    System.out.println("How many likes did your post last week get? ");
    int b = scan.nextInt();
    
    double c = (a+b)/2;
    
    System.out.println("Your average number of likes is: " + c );
    
  }
}
