char getGrade(int a, int b, int c) {
  int average = (a + b + c) / 3;
  
  if (average <= 100 && average >= 90) {
    return 'A';
  } if (average < 90 && average >= 80) {
    return 'B';
  } if (average < 80 && average >= 70) {
    return 'C';
  } if (average < 70 && average >= 60) {
    return 'D';
  } else {
    return 'F';
  }
}
