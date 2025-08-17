import java.util.Scanner;

public class IHateThisCodeOEZ
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter a number");
        int num = scan.nextInt();
        int zero=0;
        int odd=0;
        int even=0;
        
        
        while(num>0)
        {
            if(num%10==0)
            {
                zero++;
            }
            else if(num%2==0)
            {
                even++;
            }
            else
            {
                odd++;
            }
        num = num/10;
        }
        
        System.out.println(zero);
        System.out.println(odd);
        System.out.println(even);
        
        
    }
}