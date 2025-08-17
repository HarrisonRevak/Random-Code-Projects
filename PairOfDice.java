public class PairOfDice
{
    private Die die1, die2;
    
    public PairOfDice()
    {
        die1 = new Die();
        die2 = new Die();
    }
    
    public int roll()
    {
        return die.roll() + die2.roll();
    }
    
    public String toString()
    {
        return "Die1="+die1 +"Die2="+die2;
    }
}