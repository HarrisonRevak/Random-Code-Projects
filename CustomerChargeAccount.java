import java.util.*;

public class CustomerChargeAccount{
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    
    double c = 0;
    double d = 0;
    
    System.out.println("How much is your due amount?");
    double a = scan.nextInt();
    
    System.out.println("How much are you going to give?");
    double b = scan.nextInt();
    
    if(a==b){
        System.out.println("Nothing is owed");
    }
    
    if(b>a){
        c = b-a;
        System.out.println("You have $ "+ c + " credit in your account");
        
    }
    
    if(a>b){
        d = a-b;
        d*=1.02;
        System.out.println("Your new balance is $" + d);
    }
    
  }
}
