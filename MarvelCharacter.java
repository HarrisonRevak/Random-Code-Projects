public class MarvelCharacter{
    
    private String name, power;
    private int comics;
    private static int num;
    
    public MarvelCharacter(){
        num++;
    }
    
    public MarvelCharacter(String names, String powers, int comicsAppeared){
        num++;
        name = names;
        power = powers;
        comics = comicsAppeared;
    }
    
    public static int getNumCharacters(){
        return num;
    }
    
    public String getName(){
        return name;
    }
    
    public String getPower(){
        return power;
    }
    
    public int getComicsAppeared(){
        return comics;
    }
    
    public void changePower(String newPower){
        power = newPower;
    }
    
    public void setComicsAppeared(int newComicsAppeared){
        comics = newComicsAppeared;
    }
    
    public String toString(){
        return "Name: " + name + " Power: " + power + " Comics Appeared in: " + comics;
    }
}