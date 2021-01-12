import unittest


class CountryData(unittest.TestCase):
    def get_info_for_year(self, year):
        """
        List should have country,
        total visits, total nights,
        total spend, and average stay duration
        """

    def info_for_year_and_quarter(self, year, quarter):
        """
        List should have three positive values:
        total visits, total nights, total spend
        """

    def get_travel_purpose_vals(self):
        """
        List should have only five positive
        values for travel purposes
        """


if __name__ == '__main__':
    unittest.main()
