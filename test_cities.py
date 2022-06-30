import unittest
from cities import city

class CitiesTestCase(unittest.TestCase):
	def test_cities_function(self):
		city_return = city("dallas","united states of america")
		self.assertEqual(city_return, 'Dallas, United States Of America')
	def test_cities_state_function(self):
		city_state_return = city("dallas", "united states of america","texas")
		self.assertEqual(city_state_return,"Dallas, Texas, United States Of America")
unittest.main()