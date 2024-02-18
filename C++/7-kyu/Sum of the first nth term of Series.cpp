#include <iostream>
#include <iomanip>
#include <sstream> 

std::string seriesSum(int n) {
    double sum = 0.0;

    for (int i = 0; i < n; ++i) {
        sum += 1.0 / (1 + i * 3);
    }

    std::ostringstream resultStream;
    resultStream << std::fixed << std::setprecision(2) << sum;
    std::string result = resultStream.str();

    return result;
}
