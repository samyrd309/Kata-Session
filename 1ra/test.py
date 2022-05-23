import unittest
from unittest import result
import main
 
class TestTemperature(unittest.TestCase):
    def test_K_to_C(self):
        b = main.Temperature(0, '°K')
        output = b.Convert('°C')
        self.assertEqual(output, (-273.15, '°C'))
    def test_K_to_F(self):
        b = main.Temperature(0, '°K')
        output = b.Convert('°F')
        self.assertEqual(output, (-459.67, '°F'))
    def test_C_to_F(self):
        b = main.Temperature(0, '°C')
        output = b.Convert('°F')
        self.assertEqual(output, (32, '°F'))
    def test_C_to_K(self):
        b = main.Temperature(0, '°C')
        output = b.Convert('°K')
        self.assertEqual(output, (273.15, '°K'))
    def test_F_to_K(self):
        b = main.Temperature(0, '°F')
        output = b.Convert('°K')
        self.assertEqual(output, (255.37, '°K'))
    def test_F_to_C(self):
        b = main.Temperature(0, '°F')
        output = b.Convert('°C')
        self.assertEqual(output, (-17.78, '°C')) 
        
    def test_add(self):
        a = main.Temperature(2, '°K')
        b = main.Temperature(-2, '°C')
        b = b.Convert(a.TempScale)
        b = b[0]
        output = a.add(b)
        self.assertEqual(output, 273.15)
        
    def test_sub(self):
        a = main.Temperature(2, '°K')
        b = main.Temperature(-2, '°C')
        b = b.Convert(a.TempScale)
        b = b[0]
        output = a.sub(b)
        self.assertEqual(output, -269.15)
        
    def test_mul(self):
        a = main.Temperature(2, '°K')
        b = main.Temperature(-2, '°C')
        b = b.Convert(a.TempScale)
        b = b[0]
        output = a.mul(b)
        self.assertEqual(output, 542.3)
        
    def test_div(self):
        a = main.Temperature(2, '°K')
        b = main.Temperature(-2, '°C')
        b = b.Convert(a.TempScale)
        b = b[0]
        output = a.div(b)
        self.assertEqual(output, 0.00) 
        
        
if __name__ == '__main__':
    unittest.main()