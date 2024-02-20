#include <cmath>

class Bouncingball {
public:
    static int bouncingBall(double h, double bounce, double window) {
        if (h > 0 && (bounce > 0 && bounce < 1) && window < h) {
            int passes = 1;

            while (h * bounce > window) {
                passes += 2;
                h *= bounce;
            }

            return passes;
        } else {
            return -1;
        }
    }
};
