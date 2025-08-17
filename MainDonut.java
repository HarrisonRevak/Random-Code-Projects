import java.util.Scanner;

public class MainDonut
{
    public static void main(String[] args) {
        int glazeduser;
        int longjohnsuser;
        int creamfilleduser;
        
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter how many Glazed");
        glazeduser = scan.nextInt();
        System.out.println("Enter how many LongJohns");
        longjohnsuser = scan.nextInt();
        System.out.println("Enter how many Cream Filled");
        creamfilleduser = scan.nextInt();
        
        DonutOrder donut = new DonutOrder(glazeduser, longjohnsuser, creamfilleduser);
        
        double totalcost = donut.totalCost();
        
        System.out.println( donut.toString());
        System.out.printf("%.2f", totalcost);
    }
}