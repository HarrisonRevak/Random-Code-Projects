public class DreamDriver{
    
    public static void main(String[] args){
        DreamVacation dream = new DreamVacation();
        DreamVacation dreamer = new DreamVacation(5000, "Switzerland");
        
        dream.changeName("Germany");
        dream.changeCost(2340.51);
        
        System.out.println("1st location: " + dream.getName());
        System.out.println("1st cost: " + dream.getCost());
        System.out.println("2nd location: " + dreamer.getName());
        System.out.println("2nd cost: " + dreamer.getCost());
    }
}