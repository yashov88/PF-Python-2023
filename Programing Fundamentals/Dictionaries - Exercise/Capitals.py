countries = input().split(", ")
capitals = input().split(", ")

# capital_by_country = {countries[idx]: capitals[idx] for idx in range(len(countries))}
#
# for country, capital in capital_by_country.items():
#     print(f"{country} -> {capital}")

capital_by_country = dict(zip(countries, capitals))

for country, capital in capital_by_country.items():
    print(f"{country} -> {capital}")
