public class ArrayMethods{
    
    public static void printOnOne(String a[]){
        for(int i=0; i<a.length; i++){
            System.out.print(a[i] + "  ");
        }
        
    }
    
    public static void printIt(String a[]){
        for(int i=0; i<a.length; i++){
            System.out.println(a[i] + " ");
        }
        
    }
    
    public static int addIt(int a[]){
        int total = 0;
        for(int i=0; i<a.length; i++){
            total += a[i];
        }
        return total;
    }
    
    public static double addIt(double a[]){
        double total=0;
        for(int i=0; i<a.length; i++){
            total += a[i];
        }
        return total;
    }
    
    public static double average(int a[]){
        int count =0;
        double total = 0;
        for(int i=0; i<a.length; i++){
            count++;
            total += a[i];
        }
        double average = total/count;
        return average;
    }
    
    public static double average(double a[]){
        int count =0;
        double total = 0;
        for(int i=0; i<a.length; i++){
            count++;
            total += a[i];
        }
        double average = total/count;
        return average;
    }
    
}