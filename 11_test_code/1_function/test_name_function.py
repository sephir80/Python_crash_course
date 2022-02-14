import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test per 'name_function.py'."""

    def test_first_last_name(self):
        """Nomi cone 'Alesssandro Tognon' funzionano?"""
        formatted_name = get_formatted_name('Alessandro', 'Tognon')
        self.assertEqual(formatted_name, 'Alessandro Tognon')

    def test_first_last_middle_name(self):
        """Nomi come 'Gustavo Primo Mela funzionano?"""
        formatted_name = get_formatted_name('gustavo', 'mela', 'primo')
        self.assertEqual(formatted_name, 'Gustavo Primo Mela')


if __name__ == '__main__':
    unittest.main()
