public class DreamVacation
{
    private String name;
    private double cost;
    
    public DreamVacation(){
    }
    
    public DreamVacation(double a, String b){
        cost = a;
        name = b;
    }
    
    public String getName(){
        return name;
    }
    
    public double getCost(){
        return cost;
    }
    
    public void changeName(String a){
        name = a;
    }
    
    public void changeCost(double a){
        cost = a;
    }
}