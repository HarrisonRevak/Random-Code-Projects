public class MarchMadness{
    
    private int onePointers, twoPointers, threePointers, onesAttempted, twosAttempted, threesAttempted;
    
    public MarchMadness(int a, int b, int c, int d, int e, int f){
        
        onePointers = a;
        twoPointers = b;
        threePointers = c;
        onesAttempted = d;
        twosAttempted = e;
        threesAttempted = f;
    }
    
    public int score(){
        int score = (onePointers + twoPointers + threePointers);
        return score;
    }
    
    public double percentages(String type){
        if(type.equals("free throw")){
            double percentage = ((double)onePointers/onesAttempted)*100;
            return percentage;
        }
        else if(type.equals("two-pointer")){
            double percentage = ((double)twoPointers/twosAttempted)*100;
            return percentage;
        }
        else if(type.equals("three-pointer")){
            double percentage = ((double)threePointers/threesAttempted)*100;
            return percentage;
        }
        else{
            double percentage = 0;
            return percentage;
        }
    }
    
    public static void message(){
        System.out.println("Welcome to March Madness!");
    }
}