public class CardDriver
{
    public static void main(String[] args) {
        
        
        for(int x=0; x<10; x++){
            CardHand cards1 = new CardHand();
            System.out.println(cards1.toString());
            if(cards1.cardSame()){
                System.out.println("Match :)");
            }
            else{
                System.out.println("Not match :(");
            }
        }
        
        
        
        
    }
}
