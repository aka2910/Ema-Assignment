import csv
import time

data = csv.reader(open("school_data.csv", "r"))
data = list(data)
header = data[0]
data = data[1:]

# pre processing
processed_data = []
for row in data:
    school = row[3].lower()
    city = row[4].lower()
    state = row[5].lower()
    tokenized_school = school.split()
    tokenized_city = city.split()
    tokenized_state = state.split()
    tokens = set(tokenized_school + tokenized_city + tokenized_state)
    processed_data.append((tokens, row[3], row[4], row[5]))

def levenshtein_distance(s1, s2):
    """
    Calculates the levenshtein distance between two strings
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    previous_row = list(range(len(s2) + 1))
    current_row = [0] * (len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row[0] = i + 1
        for j, c2 in enumerate(s2):
            cost = -1 if c1 == c2 else 1
            current_row[j + 1] = min(current_row[j] + 1, previous_row[j + 1] + 1, previous_row[j] + cost)
        previous_row, current_row = current_row, previous_row
    return previous_row[-1]


def search_schools(query):
    """
    Returns a list of schools that match the query
    """
    t = time.time()
    # use some sort of ranking algorithm
    query_tok = query.lower()
    query_tok = query_tok.split()
    query_tok = set(query_tok)

    school_results = []
    for tokens, school, city, state in processed_data:
        # Create a copy of the query tokens for this school
        query_tok_copy = set(query_tok)
        
        intersection = tokens.intersection(query_tok_copy)
        intersection_score = len(intersection) * 4

        levenshtein_score = 0
        for token in query_tok_copy:
            tokenized_school = school.split()
            tokenized_city = city.split()

            school_min_distance = min([levenshtein_distance(token, t) for t in tokenized_school]) * 0.5
            city_min_distance = min([levenshtein_distance(token, t) for t in tokenized_city]) 

            # Accumulate the Levenshtein scores for school and city
            levenshtein_score += school_min_distance + city_min_distance

        levenshtein_score /= len(query_tok_copy)

        score = intersection_score - levenshtein_score
        school_results.append((score, school, city, state))
    
    school_results.sort(reverse=True)
    print(f'Results for "{query}"')
    if len(school_results) == 0:
        print("No results found")
    else:
        for i, (_, school, city, state) in enumerate(school_results[:3]):
            print(f"{i+1}. {school}\n{city}, {state}")

    # print(f"Search took {time.time() - t} seconds")


if __name__ == "__main__":
    search_schools("elementary school highland park")
    print("------------------")
    search_schools("jefferson belleville")
    print("------------------")
    search_schools("riverside school 44")
    print("------------------")
    search_schools("KUSKOKWIM")
    print("------------------")
    search_schools("foley high alabama")
    print("------------------")
    search_schools("granada charter school")
