public class HeightDriver
{
    public static void main(String[] args) {
        Height nocon = new Height(7, 8);
        
        Height kid = new Height(36);
        
        Height dolly = new Height(60);
        
        Height vern = new Height(2, 8);
        
        kid.simplify();
        dolly.simplify();
        
        System.out.println("Brenden Adams: " + nocon.toString());
        
        System.out.println("Little kid: " + kid.toString());
        
        System.out.println("Dolly Parton: " + dolly.toString());
        
        System.out.println("Vern Troyer: " + vern.toString());
        
        
        kid.add(4);
        dolly.add(vern);
        
        
        kid.simplify();
        dolly.simplify();
        
        System.out.println();
        
        System.out.println("Brenden Adams: " + nocon.toString());
        
        System.out.println("Little kid: " + kid.toString());
        
        System.out.println("Dolly Parton: " + dolly.toString());
        
        System.out.println("Vern Troyer: " + vern.toString());
    }
}