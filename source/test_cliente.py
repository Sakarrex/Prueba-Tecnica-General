import unittest
from cliente import listarProf

class test_cliente(unittest.TestCase):

    def test_cargarProf(self):
        result = listarProf()
        self.assertEqual(result.status_code,200)

if __name__ == '__main__':
    unittest.main()