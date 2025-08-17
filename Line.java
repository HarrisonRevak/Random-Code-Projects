public class Line{
    
    private double pointx1, pointx2, pointy1, pointy2;
    
    public Line(){
        pointx1 = Math.random()*100+1;
        pointx2 = Math.random()*100+1;
        pointy1 = Math.random()*100+1;
        pointy2 = Math.random()*100+1;
    }
    
    public double getDist(){
        double distance = Math.sqrt(Math.pow(pointx2 - pointx1,2) + Math.pow(pointy2 - pointy1,2));
        return distance;
    }
    
    public double getSlope(){
        double slope = (pointy2 - pointy1)/(pointx2 - pointx1);
        return slope;
    }
    
    public String toString(){
        /*System.out.println("X1: " + pointx1);
        System.out.println("Y1: " + pointy1);
        System.out.println("X2: " + pointx2);
        System.out.println("Y2: " + pointy2);*/
        return "pointx1" + pointx1 + "pointx2" + pointx2 + "pointy1" + pointy1 + "pointy2" + pointy2;
    }
    
}