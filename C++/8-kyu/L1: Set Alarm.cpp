bool set_alarm(const bool& employed,const bool& vacation) {
  if ((employed && vacation) || (!employed && !vacation) || (!employed && vacation)) {
    return false;
  }
  
  return true;
}
