public class Height{
    
    private int feet;
    private int inches;
    
    public Height(int a, int b){
        feet = a;
        inches = b;
    }
    
    public Height(int a){
        inches = a;
        feet = 0;
    }
    
    public void simplify(){
        if (inches>12){
            feet = inches/12;
            inches = inches%12;
        }
    }
    
    public void add(int a){
        inches += a;
    }
    
    public void add(Height ht){
        feet += ht.getFt();
        inches += ht.getIn();
        
    }
    
    public int getIn(){
        return inches;
    }
    
    public int getFt(){
        return feet;
    }
    
    public String toString(){
        return feet + " feet " + inches + " inches";
    }
    
    
}