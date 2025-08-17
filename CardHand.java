public class CardHand{
    
    private Card card1, card2;
    
    public CardHand(){
        
        card1 = new Card();
        card2 = new Card();
    }
    
    public boolean cardSame(){
        if(card1.cardValue() == card2.cardValue()){
            return true;
        }
        else{
            return false;
        }
        
    }
    
    public String toString(){
        return "Card 1 = " +card1 + "    Card 2 = " +card2;
    }
}