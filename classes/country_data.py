# Aidan Coyne

class CountryData:
    def __init__(self, country, num_visits, amount_spent, total_nights, purpose, stay_duration):
        self.country = country
        self.num_visits = num_visits
        self.amount_spent = amount_spent
        self.total_nights = total_nights
        self.purpose = purpose
        self.stay_duration = stay_duration

    def get_info_for_year(self, year):
        """Return data for specific year"""

    def info_for_year_and_quarter(self, year, quarter):
        """Return data for year and specific quarter"""

    def get_travel_purpose_vals(self):
        return self.purpose
