public class Testbody {
    public static void main(String[] args) {
        Body b1 = new Body(1.0, 1.0, 3.0, 4.0, 5.0, "jupiter.gif");
        Body b2 = new Body(4.0, 5.0, 3.0, 4.0, 5.0, "jupiter.gif");

        double r = b1.calcDistance(b2);
        double F = b1.calcForceExertedBy(b2);
        System.out.println(r);
        System.out.println(F);
    }
}
