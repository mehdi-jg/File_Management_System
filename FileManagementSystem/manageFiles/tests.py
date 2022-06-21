from django.test import TestCase

# Create your tests here.
import bangla
bangla_date = bangla.get_date(6,1,2022) # date, month, year
print(bangla_date)

bangla_numeric_string = bangla.convert_english_digit_to_bangla_digit("6 January 2022")
print(bangla_numeric_string)
