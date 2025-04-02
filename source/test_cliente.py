import unittest
from cliente import cargarProf

class test_cliente(unittest.TestCase):

    def test_cargarProf(self):
        result = cargarProf("c","c","c","c")
        self.assertEqual(result.status_code,200)

if __name__ == '__main__':
    unittest.main()