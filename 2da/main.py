class Temperature():
  def __init__(self, TempValue, TempScale):
    self.TempValue = TempValue
    self.TempScale = TempScale
  
  def add(self, TempValue)  :
    return self.TempValue + TempValue
  def sub(self, TempValue)  :
    return self.TempValue - TempValue
  def mul(self, TempValue)  :
    return self.TempValue *  TempValue
  def  div(self, TempValue)  :
    return round(self.TempValue / TempValue, 2)
  
  def Convert(self, TempScale):
    if self.TempScale == TempScale:
      return self.TempScale
    else:
      if self.TempScale == '°K' and TempScale == '°C':
        self .TempValue = round(self.TempValue - 273.15, 2)
        self.TempScale = TempScale
        return self.TempValue, self.TempScale
      if self.TempScale == '°K' and TempScale == '°F':
        self.TempValue = round((self.TempValue - 273.15) * 9/5 + 32,2)
        self.TempScale = TempScale
        return self.TempValue, self.TempScale
      if self.TempScale == '°F' and TempScale == '°C':
        self.TempValue = round((self.TempValue  -  32) * 5/9 ,  2)
        self.TempScale = TempScale
        return self.TempValue, self.TempScale
      elif self.TempScale == '°F' and TempScale == '°K':
        self.TempValue = round((self.TempValue -  32) * 5/9 + 273.15 ,  2)
        self.TempScale = TempScale
        return self.TempValue, self.TempScale
      elif self.TempScale == '°C' and TempScale == '°K':
        self.TempValue = round(self.TempValue + 273.15 ,  3)
        self.TempScale = TempScale
        return self.TempValue, self.TempScale
      elif self.TempScale == '°C' and TempScale == '°F':
        self.TempValue = round((self.TempValue*  9/5) + 32,  2)
        self.TempScale = TempScale
        return self.TempValue, self.TempScale