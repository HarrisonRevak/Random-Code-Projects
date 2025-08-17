import java.util.Scanner;

public class ScanThing{
    
    public static void main(String[] args){
        Scanner scan = new Scanner(System. in);
        
        System.out.println("What is your name? ");
        String name = scan.nextLine();
        
        System.out.println("How many hours did you work? ");
        Double a = scan.nextDouble();
        
        System.out.println("How much do you make per hour? ");
        Double b = scan.nextDouble();
        
        Double c = a*b;
        
        System.out.println("Your gross income for the week is $" + c);
        
    }
}