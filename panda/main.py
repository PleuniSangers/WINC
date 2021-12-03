import pandas as pd
pd.set_option('max_rows', 99999) 
pd.set_option('max_colwidth', 400)
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_birth_rate")
countries = tables[0]
countries.columns = ["country", 'WB', "OECD", "CIA13","CIA14","CIA20","PRB20"]
print(countries)

