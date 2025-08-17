public class AdditionPattern{
    public int firstnum, currentnum, itter;
    
    public AdditionPattern(int a, int b){
        firstnum = a;
        currentnum = a;
        itter = b;
    }
    
    public int currentNumber(){
        return currentnum;
    }
    
    public void next(){
        currentnum += itter;
    }
    
    public void prev(){
        if(currentnum != firstnum){
            currentnum -= itter;
        }
    }
}