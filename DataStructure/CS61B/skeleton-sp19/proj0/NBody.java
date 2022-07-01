/**
 * NBody
 */
public class NBody {
    public static double readRadius(String fileName) {
        In in = new In(fileName);
        int num = in.readInt();
        double radius = in.readDouble();
        return radius;
    }

    public static Body[] readBodies(String fileName) {
        In in = new In(fileName);
        int num = in.readInt();
        double radius = in.readDouble();
        Body[] bodys = new Body[num]; // 问题
        for (int i = 0; i < num; i++) {
            double xp = in.readDouble();
            double yp = in.readDouble();
            double vx = in.readDouble();
            double vy = in.readDouble();
            double m = in.readDouble();
            String img = in.readString();
            bodys[i] = new Body(xp, yp, vx, vy, m, img);
        }
        return bodys;
    }

    public static void main(String[] args) {
        double T = Double.parseDouble(args[0]);
        double dt = Double.parseDouble(args[1]);
        String filename = args[2];

        double r = readRadius(filename);
        Body[] bodys = readBodies(filename);

        // 画宇宙
        StdDraw.setXscale(-r, r);
        StdDraw.setYscale(-r, r);
        StdDraw.enableDoubleBuffering();

        double time = 0;
        int num = bodys.length;
        while (time <= T) {
            double[] xForces = new double[num];
            double[] yForces = new double[num];
            for (int i = 0; i < num; i++) {
                xForces[i] = bodys[i].calcNetForceExertedByX(bodys);
                yForces[i] = bodys[i].calcNetForceExertedByY(bodys);
            }
            for (int j = 0; j < num; j++) {
                bodys[j].update(dt, xForces[j], yForces[j]);
            }
            // 背景
            StdDraw.picture(0, 0, "images/starfield.jpg");

            // 画出所有的Bodys
            for (Body allBody : bodys) {
                allBody.draw();
            }
            StdDraw.show();
            StdDraw.pause(10);
            time += dt;
        }

        StdOut.printf("%d\n", bodys.length);
        StdOut.printf("%.2e\n", r);
        for (int i = 0; i < bodys.length; i++) {
            StdOut.printf("%11.4e %11.4e %11.4e %11.4e %11.4e %12s\n",
                    bodys[i].xxPos, bodys[i].yyPos, bodys[i].xxVel,
                    bodys[i].yyVel, bodys[i].mass, bodys[i].imgFileName);

        }
    }

}