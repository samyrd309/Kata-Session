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
    return round(self.TempValue  / TempValue, 2)
  
  def convert(self, TempScale):
    if self.TempScale == TempScale:
      return self.TempValue, self.TempScale
    else:
      if TempScale == TemperatureScale.Kelvin:
        if self.TempScale == TemperatureScale.Celsius:
          self.TempValue = round(self.TempValue + 273.15,2)
          self.TempScale == TemperatureScale.Kelvin
          return self.TempValue, TempScale
        if self.TempScale == TemperatureScale.Fahrenheit:
          self.TempValue = round((self.TempValue - 32) *  5/9 + 273.15,2)
          self.TempScale == TemperatureScale.Kelvin
          return self.TempValue, TempScale
      if TempScale == TemperatureScale.Celsius:
        if self.TempScale == TemperatureScale.Fahrenheit:
          self.TempValue = round((self.TempValue - 32) * 5/9,2)
          self.TempScale == TemperatureScale.Celsius
          return self.TempValue, TempScale
        if self.TempScale == TemperatureScale.Kelvin:
          self.TempValue = round(self.TempValue - 273.15,2)
          self.TempScale == TemperatureScale.Celsius
          return self.TempValue, TempScale
      if TempScale == TemperatureScale.Fahrenheit:
        if self.TempScale == TemperatureScale.Celsius:
          self.TempValue = round((self.TempValue * 9/5) + 32 ,2)
          self.TempScale == TemperatureScale.Fahrenheit
          return self.TempValue, TempScale
        if self.TempScale == TemperatureScale.Kelvin:
          self.TempValue = round((self.TempValue - 273.15) * 9/5 + 32 ,2)
          self.TempScale == TemperatureScale.Fahrenheit
          return self.TempValue, TempScale
        
        