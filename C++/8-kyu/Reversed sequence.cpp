std::vector<int> reverseSeq(int n) {
  std::vector<int> reversedVector;
  
  for (int i = n; i > 0; i--) {
    reversedVector.push_back(i); 
  }
  
  return reversedVector;
}
