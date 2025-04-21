from animal import animal
from hyena import hyena
from lion import lion
from bear import bear
from tiger import tiger

# create lists of the species
list_of_hyenas = hyena()
list_of_lions = Lion()
list_of_tigers = tigers()
list_of_bears = bears()

#todays' date
current_date = date.today()
current_year = current_date.year

def date_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)
