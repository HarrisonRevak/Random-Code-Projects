
/*
Online Java - IDE, Code Editor, Compiler

Online Java is a quick and easy tool that helps you to build, compile, test your programs online.
*/

public class Arraysthingy
{
    public static void main(String[] args) {
        String [] teachers = {"Flispart", "Scott", "Munoz", "Burres", "Ponders", "Haeberlin", "Kelley"};
        
        System.out.println("My 2nd period teacher is "+ teachers[1]);
        
        int [] eimacs = new int[4];
        
        eimacs[0]=10;
        eimacs[1]=6;
        eimacs[2]=8;
        eimacs[3]=10;
        
        double sum = 0;
        
        for(int x=0; x<eimacs.length; x++){
            sum+= eimacs[x];
        }
        
        System.out.println(sum/eimacs.length);
    }
}
