public class DriverMarvel
{
    public static void main(String[] args) {
        MarvelCharacter avenger1 = new MarvelCharacter();
        
        MarvelCharacter spiderMan = new MarvelCharacter("SpiderMan", "Webbing Projection", 300);
        
        MarvelCharacter symbiote = new MarvelCharacter("Venom", "Shapeshifting", 144);
        
        System.out.println(symbiote.getName());
        
        symbiote.changePower("Webbing Projection");
        
        spiderMan.setComicsAppeared(spiderMan.getComicsAppeared()+1);
        
        MarvelCharacter iron = new MarvelCharacter("Tony Stark", "Iron Suit", 2579);
        
        System.out.println(avenger1.toString());
        System.out.println(spiderMan.toString());
        System.out.println(symbiote.toString());
        System.out.println(iron.toString());
        
        System.out.println("Num of characters created: " + MarvelCharacter.getNumCharacters());
    }
}