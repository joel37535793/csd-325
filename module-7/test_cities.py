import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = city_country("Santiago", "Chile")
        self.assertEqual(formatted_name, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
