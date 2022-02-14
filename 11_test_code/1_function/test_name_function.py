import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test per 'name_function.py'."""

    def test_first_last_name(self):
        """Nomi cone 'Alesssandro Tognon' funzionano?"""
        formatted_name = get_formatted_name('Alessandro', 'Tognon')
        self.assertEqual(formatted_name, 'Alessandro Tognon')


if __name__ == '__main__':
    unittest.main()
