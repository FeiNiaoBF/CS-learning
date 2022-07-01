
public class Body {
    public double xxPos; // 它当前的 x 位置
    public double yyPos; // 它当前的 y 位置
    public double xxVel; // 它在 x 方向上的当前速度
    public double yyVel; // 它在 y 方向上的当前速度
    public double mass; // 它的质量
    public String imgFileName;
    private static final double G = 6.67e-11;

    public Body(double xP, double yP,
            double xV, double yV,
            double m,
            String img) {
        xxPos = xP;
        yyPos = yP;
        xxVel = xV;
        yyVel = yV;
        mass = m;
        imgFileName = img;
    }

    public Body(Body b) {
        xxPos = b.xxPos;
        yyPos = b.yyPos;
        xxVel = b.xxVel;
        yyVel = b.yyVel;
        mass = b.mass;
        imgFileName = b.imgFileName;
    }

    // 两个星球的距离
    public double calcDistance(Body body) {
        return Math.sqrt((Math.pow((body.xxPos - xxPos), 2)) + (Math.pow(body.yyPos - yyPos, 2)));
    }

    // 两个星球的万有引力
    public double calcForceExertedBy(Body b) {
        double r = calcDistance(b);
        return (G * mass * b.mass) / Math.pow(r, 2);
    }

    // 对引力的x轴和y轴的分力
    public double calcForceExertedByX(Body b) {
        double dx = b.xxPos - xxPos;
        double r = calcDistance(b);
        return calcForceExertedBy(b) * dx / r;
    }

    public double calcForceExertedByY(Body b) {
        double dy = b.yyPos - yyPos;
        double r = calcDistance(b);
        return calcForceExertedBy(b) * dy / r;
    }

    // 计算在星系网的环境下对行星施加的力
    public double calcNetForceExertedByX(Body[] allBodys) {
        double totalForce = 0;
        for (Body bodys : allBodys) {
            if (this.equals(bodys)) {
                continue;
            }
            totalForce += calcForceExertedByX(bodys);
        }
        return totalForce;
    }

    public double calcNetForceExertedByY(Body[] allBodys) {
        double totalForce = 0;
        for (Body bodys : allBodys) {
            if (this.equals(bodys)) {
                continue;
            }
            totalForce += calcForceExertedByY(bodys);
        }
        return totalForce;
    }

    // 更新星体的加速度，速度，位置
    public void update(double dt, double fx, double fy) {
        double ax = fx / mass;
        double ay = fy / mass;
        xxVel += dt * ax;
        yyVel += dt * ay;
        xxPos += xxVel * dt;
        yyPos += yyVel * dt;
    }

    // 绘画星球
    public void draw() {
        StdDraw.picture(xxPos, yyPos, "images/" + imgFileName);
    }
}
