import java.util.*;

public class NameComparison {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    
    String a,b;
    boolean c = false;
    boolean d = false;
    boolean e = false;
    
    System.out.println("Enter your name: ");
    a = scan.nextLine();
    
    System.out.println("Enter other name: ");
    b = scan.nextLine();
    
    if(a.compareTo(b) < 0){
        c = true;
    }
    
    else if(a.compareTo(b) == 0){
        d = true;
    }
    
    else if(a.compareTo(b) >0){
        e = true;
    }
    
    int x = a.length();
    int y = b.length();
    int z = 0;
    
    if(x>y){
        z = x-y;
    }
    
    if(x<y){
        z = y-x;
    }
    
    if(c == true){
        System.out.print( a.toUpperCase() + " comes before " + b.toUpperCase());
    }
    else if(d == true){
        System.out.print("you have the same name");
    }
    else if(e == true){
        System.out.print( b.toUpperCase() + " comes before " + a.toUpperCase());
    }
    
    if(x>y){
        System.out.println(" " + a + " has " + z + " more character(s) than " + b);
    }
    else if(y>x){
        System.out.println(" " + b + " has " + z + " more character(s) than " + a);
    }
    else if(x == y){
        System.out.println("Your names are the same length");
    }
    
    
  }
}
