import java.util.Scanner;

public class OddEvenZero
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter a number");
        int num = scan.nextInt();
        String wordnum = Integer.toString(num);
        int wordlengthnum = wordnum.length();
        int othernum;
        int zero=0;
        int odd=0;
        int even=0;
        

        
        for(int counter=0; counter<wordlengthnum; counter++)
        {
            char numbees = wordnum.charAt(counter);
            if(numbees==48)
            {
                zero+=1;
            }
            else if(numbees%2==0)
            {
                even+=1;
            }
            else if(numbees%2==1)
            {
                odd+=1;
            }
        }
        
        System.out.println(zero);
        System.out.println(even);
        System.out.println(odd);
    }
}
