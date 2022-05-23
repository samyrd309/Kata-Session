class Temperature():
  def __init__(self, TempValue, TempScale):
    self.TempValue = TempValue
    self.TempScale = TempScale
  
  def Convert(self, TempScaleA):
    if TempScaleA == '°C':
      if self.TempScale =='°K':
        self.TempValue = round(self.TempValue - 273.15, 2)
        self.TempScale = '°C'
        return self.TempValue, self.TempScale
      if self.TempScale == '°F':
        self.TempValue = round((self.TempValue - 32) * 5/9,2) 
        self.TempScale = '°C'
        return self.TempValue, self.TempScale
    elif TempScaleA == '°K':
      if self.TempScale =='°C':
        self.TempValue = round(self.TempValue + 273.15, 2)
        self.TempScale = '°K'
        return self.TempValue, self.TempScale
      if self.TempScale == '°F':
        self.TempValue = round((self.TempValue - 32) * 5/9 + 273.15,2)
        self.TempScale = '°K'
        return self.TempValue, self.TempScale
    elif TempScaleA == '°F':
      if self.TempScale =='°K':
        self.TempValue = round((self.TempValue - 273.15) * 9/5 + 32 ,2)
        self.TempScale = '°F'
        return self.TempValue, self.TempScale
      if self.TempScale == '°C':
        self.TempValue = round((self.TempValue * 9/5) + 32,2)
        self.TempScale = '°F'
        return self.TempValue, self.TempScale 
    
  def add(self, b):
    return self.TempValue + b
  
  def sub(self, b):
    return self.TempValue - b
  
  def mul(self, b):
    return self.TempValue * b
  
  def div(self, b):
    return self.TempValue // b        