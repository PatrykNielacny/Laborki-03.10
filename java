import java.io.FileNotFoundException;
import java.io.PrintWriter;

class Pixel {
    public int x;
    public int y;

    public Pixel(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class RGB {
    public int r;
    public int g;
    public int b;

    public RGB(int red, int green, int blue) {
        this.r = red;
        this.g = green;
        this.b = blue;
    }
}

class BitmapImage {
    public int width;
    public int height;
    public RGB[][] bmp;

    public BitmapImage(int width, int height) {
        this.width = width;
        this.height = height;
        bmp = new RGB[width][height];
    }

    public void setPixelColor(Pixel p, RGB color) {
        bmp[p.x][p.y] = color;
    }

    public void drawPolish() {
        RGB red = new RGB(255, 0, 0);
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                setPixelColor(new Pixel(x, y), red);
            }
        }
        RGB white = new RGB(255, 255, 255);
        for (int y = 0; y < this.height; y++) {
            for (int x = 0; x < this.width; x++) {
                setPixelColor(new Pixel(x, y / 2), white);
            }
        }
    }

        public void drawGermany() {
            RGB yellow = new RGB ( 255, 255 ,0);
            for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                    setPixelColor(new Pixel(x, y), yellow);
                }
            }
            RGB red = new RGB(255, 0, 0);
            for (int y = 0; y < this.height; y++) {
                for (int x = 0; x < this.width; x++) {
                    setPixelColor(new Pixel(x, y * 2/3), red);
                }
            }
            RGB black = new RGB(0, 0, 0);
            for (int y = 0; y < this.height; y++) {
                for (int x = 0; x < this.width; x++) {
                    setPixelColor(new Pixel(x, y * 1/3), black);
                }
            }
        }

    public void drawUkraine() {
        RGB yellow = new RGB(255, 255, 0);
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                setPixelColor(new Pixel(x, y), yellow);
            }
        }
        RGB blue = new RGB(0, 0, 255);
        for (int y = 0; y < this.height; y++) {
            for (int x = 0; x < this.width; x++) {
                setPixelColor(new Pixel(x, y / 2), blue);
            }
        }
    }

    public void saveToFile(String fname) {
        PrintWriter out;
        try {
            out = new PrintWriter(fname + ".ppm");
            out.println("P3");
            out.println(width + " " + height);
            out.println(255);
            for (int y = 0; y < this.height; y++) {
                for (int x = 0; x < this.width; x++) {
                    out.println(bmp[x][y].r + " " + bmp[x][y].g + " " + bmp[x][y].b);
                }
            }
            out.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Polska");
        BitmapImage polska = new BitmapImage(800, 500);
        polska.drawPolish();
        polska.saveToFile("polska");

        System.out.println("Niemcy");
        BitmapImage Niemcy = new BitmapImage(800, 500);
        polska.drawGermany();
        polska.saveToFile("Niemcy");

        System.out.println("Ukraina");
        BitmapImage Ukraina = new BitmapImage(800, 500);
        polska.drawUkraine();
        polska.saveToFile("Ukraina");
    }
}
