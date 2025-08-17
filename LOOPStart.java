import java.util.Scanner;

public class LOOPStart{
    
    public static void main(String[] args){
        Scanner scan = new Scanner(System. in);
        
        for(int x = 1; x<=10; x++){
            System.out.println(x);
        }
        
        for(int x = 1; x<=10; x++){
            System.out.print(x);
        }
        
        System.out.println();
        
        for(int x = 10; x>=1; x--){
            System.out.print(x);
        }
        System.out.println();
        
        System.out.println("How high do you want me to count? ");
        int y = scan.nextInt();
        
        System.out.println();
        
        for(int x = 1; x<=y; x++){
            System.out.print(x);
        }
        System.out.println();
        
        System.out.println("What multiples would you like to know?");
        int z = scan.nextInt();
        
        for(int x = 1; x<=10; x++){
            System.out.print(z*x);
            System.out.print("");
        }
    }
}