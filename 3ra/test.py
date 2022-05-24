import unittest
from main import Temperature, TemperatureScale

class TestTemperature(unittest.TestCase):
  def test_convert_K_to_K(self):
    b = Temperature(2, TemperatureScale.Kelvin)
    output = b.convert(TemperatureScale.Kelvin)
    self.assertEqual(output, (2, TemperatureScale.Kelvin))
    
  def test_convert_C_to_K(self):
    b = Temperature(2, TemperatureScale.Celsius)
    output = b.convert(TemperatureScale.Kelvin)
    self.assertEqual(output, 'celsius to kelvin')
    
  def test_convert_F_to_K(self):
    b = Temperature(2, TemperatureScale.Fahrenheit)
    output = b.convert(TemperatureScale.Kelvin)
    self.assertEqual(output, 'fahrenheit to kelvin')
    
  def test_convert_F_to_C(self):
    b = Temperature(2, TemperatureScale.Fahrenheit)
    output = b.convert(TemperatureScale.Celsius)
    self.assertEqual(output, 'fahrenheit to celsius')

  def test_convert_K_to_C(self):
    b = Temperature(2, TemperatureScale.Kelvin)
    output = b.convert(TemperatureScale.Celsius)
    self.assertEqual(output, 'kelvin to celsius')

  def test_convert_C_to_F(self):
    b = Temperature(2, TemperatureScale.Celsius)
    output = b.convert(TemperatureScale.Fahrenheit)
    self.assertEqual(output, 'celsius to fahrenheit')

  def test_convert_K_to_F(self):
    b = Temperature(2, TemperatureScale.Kelvin)
    output = b.convert(TemperatureScale.Fahrenheit)
    self.assertEqual(output, 'kelvin to fahrenheit')
    
    
if __name__ == '__main__':
    unittest.main()