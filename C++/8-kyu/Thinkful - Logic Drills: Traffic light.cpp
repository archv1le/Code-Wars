#include <string>

std::string update_light(std::string current) {
  switch (current[0]) {
    case 'g':  
      return "yellow";
    case 'y':  
      return "red";
    case 'r':  
      return "green";
    default:
      return "invalid_state";
  }
}
