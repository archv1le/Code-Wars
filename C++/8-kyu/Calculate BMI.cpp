#include <string>

std::string bmi(double w, double h) {
  float BMI = w / (h * h);
  
  if (BMI <= 18.5) {
    return "Underweight";
  } else if (BMI <= 25) {
    return "Normal";
  } else if (BMI <= 30) {
    return "Overweight";
  }
  
  return "Obese";
}
