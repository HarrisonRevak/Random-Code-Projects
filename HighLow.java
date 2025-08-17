import java.util.Scanner;
import java.util.Random;

public class HighLow
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
       

        boolean quit = false;
        boolean play = true;
        int count=0;
        int randomnum;
        int answer = 0;
       
       
        while(play = true)
        {
            quit = false;
            count=0;
            int guess=0;
            answer = 0;
            randomnum = rand.nextInt(100)+1;
           
            while(guess != randomnum)
            {
                System.out.println("Enter a number: ");
                guess = scan.nextInt();
               
                if(guess==-999){
                    play=false;
                    quit = true;
                    System.out.println("Quitter!");
                    break;
                }
                if(guess!=-999){
                    if(guess<randomnum){
                        System.out.println("Guess higher or -999 to quit");
                    }
                    else if(guess>randomnum){
                        System.out.println("Guess lower or -999 to quit");
                    }
                    else if(guess==randomnum){
                        System.out.println("CONGRATS");
                        play=false;
                    }
                }
            count++;
            }
           
            if(quit==false){
                System.out.println("It took " + count + " times!");
            }
            else if(quit==true){
                System.out.println("You gave up.");
            }
           
           
            System.out.println("Try again? 1 for yes or 2 for no");
            answer = scan.nextInt();
            if(answer==1)
            {
                play=true;
            }
            else if(answer==2)
            {
                System.out.println("Okay, bye.");
                break;
            }
        }
       
       
       
       
    }
}