import java.util.Random;

public class Card{
    
    private int num1;
    private Random rand = new Random();
    
    public Card(){
        num1 = rand.nextInt(13)+1;
    }
    
    public int cardValue(){
        return num1;
    }
    
    public String toString(){
        return "Card value ="+num1;
    }
    
}