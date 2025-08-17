public class Triangle{
    
    private int angle1, angle2, angle3;
    
    public Triangle(int x, int y, int z){
        angle1 = x;
        angle2 = y;
        angle3 = z;
    }
    
    
    public boolean isTriangle(){
        if((angle1 + angle2 + angle3) == 180){
            return true;
        }
        else{
            return false;
        }
    }
}