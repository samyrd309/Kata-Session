import unittest
from main import Temperature, TemperatureScale

class TestTemperature(unittest.TestCase):
  def test_convert_K_to_K(self):
    b = Temperature(2, TemperatureScale.Kelvin)
    output = b.convert(TemperatureScale.Kelvin)
    self.assertEqual(output, (2, TemperatureScale.Kelvin))
    
  def test_convert_C_to_C(self):
    b = Temperature(2, TemperatureScale.Celsius)
    output = b.convert(TemperatureScale.Celsius)
    self.assertEqual(output, (2, TemperatureScale.Celsius))
  
  def test_convert_F_to_F(self):
    b = Temperature(2, TemperatureScale.Fahrenheit)
    output = b.convert(TemperatureScale.Fahrenheit)
    self.assertEqual(output, (2, TemperatureScale.Fahrenheit))
    
  def test_convert_C_to_K(self):
    b = Temperature(0, TemperatureScale.Celsius)
    output = b.convert(TemperatureScale.Kelvin)
    self.assertEqual(output, (273.15, TemperatureScale.Kelvin))
    
  def test_convert_F_to_K(self):
    b = Temperature(0, TemperatureScale.Fahrenheit)
    output = b.convert(TemperatureScale.Kelvin)
    self.assertEqual(output, (255.37, TemperatureScale.Kelvin))

  def test_convert_F_to_C(self):
    b = Temperature(0, TemperatureScale.Fahrenheit)
    output = b.convert(TemperatureScale.Celsius)
    self.assertEqual(output, (-17.78, TemperatureScale.Celsius))

  def test_convert_K_to_C(self):
    b = Temperature(0, TemperatureScale.Kelvin)
    output = b.convert(TemperatureScale.Celsius)
    self.assertEqual(output, (-273.15, TemperatureScale.Celsius))
    
  def test_convert_C_to_F(self):
    b = Temperature(0, TemperatureScale.Celsius)
    output = b.convert(TemperatureScale.Fahrenheit)
    self.assertEqual(output, (32, TemperatureScale.Fahrenheit))

  def test_convert_K_to_F(self):
    b = Temperature(0, TemperatureScale.Kelvin)
    output = b.convert(TemperatureScale.Fahrenheit)
    self.assertEqual(output, (-459.67, TemperatureScale.Fahrenheit))

  def test_add(self):
      a = Temperature(2, TemperatureScale.Kelvin)
      b = Temperature(-2, TemperatureScale.Celsius)
      b = b.convert(a.TempScale)
      b = b[0]
      output = a.add(b)
      self.assertEqual(output, 273.15)   
      
  def test_sub(self):
      a = Temperature(2, TemperatureScale.Kelvin)
      b = Temperature(-2, TemperatureScale.Celsius)
      b = b.convert(a.TempScale)
      b = b[0]
      output = a.sub(b)
      self.assertEqual(output, -269.15)   
  
  def test_mul(self):
      a = Temperature(2, TemperatureScale.Kelvin)
      b = Temperature(-2, TemperatureScale.Celsius)
      b = b.convert(a.TempScale)
      b = b[0]
      output = a.mul(b)
      self.assertEqual(output, 542.3)   
      
  def test_div(self):
      a = Temperature(2, TemperatureScale.Kelvin)
      b = Temperature(-2, TemperatureScale.Celsius)
      b = b.convert(a.TempScale)
      b = b[0]
      output = a.div(b)
      self.assertEqual(output, 0.01)   
if __name__ == '__main__':
    unittest.main()