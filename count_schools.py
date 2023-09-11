import csv

data = csv.reader(open("school_data.csv", "r"))
data = list(data)
header = data[0]
data = data[1:]


# How many total schools are in this data set?
def total_schools(data):
    """
    Returns the total number of schools in the data set.
    """
    print("Total Schools:", len(data))


# How many schools are in each state?
def schools_per_state(data):
    """
    Prints the number of schools in each state.
    """
    schools_per_state = {}
    for row in data:
        state = row[5]
        schools_per_state[state] = schools_per_state.get(state, 0) + 1
    print("Schools by State:")
    for state, school in sorted(schools_per_state.items()):
        print(state, school, sep=": ")


# How many schools are in each Metro-centric locale?
def schools_per_metro(data):
    """
    Prints the number of schools in each Metro-centric locale.
    """
    schools_per_metro = {}
    for row in data:
        metro = row[-3]
        schools_per_metro[metro] = schools_per_metro.get(metro, 0) + 1
    print("Schools by Metro-centric locale:")
    for metro, school in sorted(schools_per_metro.items()):
        print(metro, school, sep=": ")


# What city has the most schools in it? How many schools does it have in it?
def most_schools_per_city(data):
    """
    Prints the city with the most schools and the number of schools in it.
    """
    schools_per_city = {}
    for row in data:
        city = row[4]
        schools_per_city[city] = schools_per_city.get(city, 0) + 1
    max_city = max(schools_per_city, key=schools_per_city.get)
    print("City with most schools:", max_city, f"({schools_per_city[max_city]} schools)")


# How many unique cities have at least one school in it?
def unique_cities(data):
    """
    Prints the number of unique cities with at least one school in it.
    """
    unique_cities = set()
    for row in data:
        city = row[4]
        unique_cities.add(city)
    print("Unique cities with at least one school:", len(unique_cities))


def print_counts():
    """
    Prints the results of the above functions.
    """
    total_schools(data)
    schools_per_state(data)
    schools_per_metro(data)
    most_schools_per_city(data)
    unique_cities(data)


if __name__ == "__main__":
    print_counts()
