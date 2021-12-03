# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
first_language_spain = 'castilian Spanish'
first_language_switzerland = 'German'
Most_prevalent_religion_Spain = 'Roman Catholic'
Most_prevalent_religion_switzerland = 'Roman Catholic'
Name_lengbt_spain = len('Spain')
Name_lenght_Switzerland = len('Switzerland')
GDP_switzerland = 590.7
Spain_GDP = 1715
Population_growth_Spain = -0.03
Population_growth_Switzerland = 0.65
population_growth = 1.00
Population_count_Spain = 47.3
Population_count_Switzerland = 8.5
print(first_language_spain == first_language_switzerland)
print(Most_prevalent_religion_Spain == Most_prevalent_religion_switzerland)
print(Name_lengbt_spain != Name_lenght_Switzerland)
print(GDP_switzerland>Spain_GDP)
print(population_growth > Population_growth_Spain and population_growth > Population_growth_Switzerland)
print(10>Population_count_Switzerland or 10>Population_count_Spain)
print((10>Population_count_Switzerland or 10>Population_count_Spain) and (10<Population_count_Spain or 10<Population_count_Switzerland))
