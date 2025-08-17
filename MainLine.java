public class MainLine
{
    public static void main(String[] args) {
        Line line = new Line();
        
        System.out.println(line.toString());
        
        System.out.println("The slope is: " + line.getSlope());
        System.out.println("The distance is: " + line.getDist());
    }
}
