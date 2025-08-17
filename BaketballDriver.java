public class BaketballDriver
{
    public static void main(String[] args) {
        MarchMadness epicgame = new MarchMadness(10, 20, 5, 15, 40, 15);
        
         MarchMadness.message();
         
         System.out.println(epicgame.score());
         
         System.out.println(epicgame.percentages("free throw"));
         System.out.println(epicgame.percentages("two-pointer"));
         System.out.println(epicgame.percentages("three-pointer"));
         
    }
}