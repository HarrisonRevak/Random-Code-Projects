public class DonutOrder{
    
    private int glazed, longjohn, creamfilled;
    
    public DonutOrder(int x1, int x2, int x3){
        
        glazed = x1;
        longjohn = x2;
        creamfilled = x3;
    }
    
    public double totalCost(){
        double total = ((glazed * 0.85) + (longjohn * 1.20) + (creamfilled * 1.55));
        return total;
    }
    
    public String toString(){
        String result = "Glazed: " + glazed + " Longjohn: " + longjohn + " Cream Filled: " + creamfilled;
        return result;
    }
}