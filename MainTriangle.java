public class MainTriangle{
    
    public static void main(String[] args){
        Triangle tri = new Triangle(60,60,60);
        boolean tried = tri.isTriangle();
        
        if(tried == true){
            System.out.println("It is a triangle");
        }
        else{
            System.out.println("It is not a triangle");
        }
    }
}