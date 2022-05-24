class TemperatureScale():
  Kelvin = 'K'
  Celsius = 'C'
  Fahrenheit = 'F'
  
class Temperature():
  def __init__(self, TempValue, TempScale):
      self.TempValue = TempValue
      self.TempScale = TempScale
  def add(self, TempValue):
    return self.TempValue + TempValue
  def  sub(self, TempValue):
    return self.TempValue - TempValue
  def mul(self, TempValue):
    return self.TempValue *  TempValue
  def div(self, TempValue):
    return self.TempValue  / TempValue
  
  def convert(self, TempScale):
    if self.TempScale == TempScale:
      return self.TempValue, self.TempScale
    else:
      if TempScale == TemperatureScale.Kelvin:
        if self.TempScale == TemperatureScale.Celsius:
          self.TempValue = self.TempValue + 273.15
          self.TempScale == TemperatureScale.Kelvin
          return self.TempValue, TempScale
        if self.TempScale == TemperatureScale.Fahrenheit:
          self.TempValue = (self.TempValue - 32) *  5/9 + 273.15
          self.TempScale == TemperatureScale.Kelvin
          return self.TempValue, TempScale
      if TempScale == TemperatureScale.Celsius:
        if self.TempScale == TemperatureScale.Fahrenheit:
          self.TempValue =(self.TempValue - 32) * 5/9
          self.TempScale == TemperatureScale.Celsius
          return self.TempValue, TempScale
        if self.TempScale == TemperatureScale.Kelvin:
          self.TempValue = self.TempValue - 273.15
          self.TempScale == TemperatureScale.Celsius
          return self.TempValue, TempScale
      if TempScale == TemperatureScale.Fahrenheit:
        if self.TempScale == TemperatureScale.Celsius:
          self.TempValue = (self.TempValue * 9/5) + 32 
          self.TempScale == TemperatureScale.Fahrenheit
          return self.TempValue, TempScale
        if self.TempScale == TemperatureScale.Kelvin:
          self.TempValue = (self.TempValue - 273.15) * 9/5 + 32 
          self.TempScale == TemperatureScale.Fahrenheit
          return self.TempValue, TempScale
        
        