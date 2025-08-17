public class ArrayMethodDriver
{
    public static void main(String[] args) {
        String a[] = {"Onion", "potato", "Chihuahua", "Blueray edition of Shrek", "Fork"};
        int b[] = new int[10];
        double c[] = new double[10];
        
        for(int i=0; i<10; i++){
            b[i] = i;
        }
        
        for(int x=0; x<50; x+=5){
            c[x/5] = x;
        }
        
        System.out.println("Print in one: ");
        
        ArrayMethods.printOnOne(a);
        
        System.out.println("");
        System.out.println("Print it: ");
        
        ArrayMethods.printIt(a);
        
        System.out.println("add it int: ");
        
        System.out.println(ArrayMethods.addIt(b));
        
        System.out.println("average int: ");
        
        System.out.println(ArrayMethods.average(b));
        
        System.out.println("");
        
        
        System.out.println("add it double: ");
        
        System.out.println(ArrayMethods.addIt(c));
        
        System.out.println("average double: ");
        
        System.out.println(ArrayMethods.average(c));
        
        
    }
}
