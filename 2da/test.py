
import unittest
from main import Temperature
#K_to_C = 0K − 273.15 = -273.1°C

class TestTemperatura(unittest.TestCase):

  #Convert Test Casese
  def test_Convert_C_to_F(self):
      b = Temperature(0, '°C')
      output = b.Convert('°F')
      self.assertEqual(output,  (32, '°F'))
  
  def test_Convert_K_to_F(self):
      b = Temperature(0, '°K')
      output = b.Convert('°F')
      self.assertEqual(output,  (-459.67, '°F'))

  def test_Convert_F_to_K(self):
      b = Temperature(0, '°F')
      output = b.Convert('°K')
      self.assertEqual(output,  (255.37, '°K'))
        

  def test_Convert_F_to_C(self):
      b = Temperature(0, '°F')
      output = b.Convert('°C')
      self.assertEqual(output,  (-17.78, '°C'))
    
  def test_Convert_C_to_K(self):
      b = Temperature(0, '°C')
      output = b.Convert('°K')
      self.assertEqual(output,  (273.15, '°K'))
      
  def test_Convert_K_to_C(self):
    b = Temperature(0, '°K')
    output = b.Convert('°C')
    self.assertEqual(output,  (-273.15, '°C'))
      
  #Celsius to Kelvin
  def test_add(self):
    a = Temperature(50, '°K')
    b = Temperature(96, '°C')
    b = b.Convert(a.TempScale)
    b = b[0]
    output = a.add(b)
    self.assertEqual(output, 419.15)
    
  def test_sub(self):
    a = Temperature(50, '°K')
    b = Temperature(96, '°C')
    b = b.Convert(a.TempScale)
    b = b[0]
    output = a.sub(b)
    self.assertEqual(output, -319.15)

  def test_mul(self):
    a = Temperature(50, '°K')
    b = Temperature(96, '°C')
    b = b.Convert(a.TempScale)
    b = b[0]
    output = a.mul(b)
    self.assertEqual(output, 18457.5)
    
  def test_div(self):
    a = Temperature(50, '°K')
    b = Temperature(96, '°C')
    b = b.Convert(a.TempScale)
    b = b[0]
    output = a.div(b)
    self.assertEqual(output, 0.14)    

      
  
  
if __name__ == '__main__':
    unittest.main()