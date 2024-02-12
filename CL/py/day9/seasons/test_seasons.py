import seasons
from datetime import date

def test_calculate_age_in_minutes():
    assert seasons.calculate_age_in_minutes(date(2000, 1, 1)) == 10439040
    assert seasons.calculate_age_in_minutes(date(2000, 2, 12)) == 12623040
