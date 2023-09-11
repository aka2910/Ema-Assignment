import csv
import time

data = csv.reader(open("school_data.csv", "r"))
data = list(data)
header = data[0]
data = data[1:]


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


def search_schools(query):
    t = time.time()
    # use some sort of ranking algorithm
    query_tok = query.lower()
    query_tok = query_tok.split()
    query_tok = set(query_tok) - set(["school"])

    school_results = []
    for tokens, school, city, state in processed_data:
        score = len(tokens.intersection(query_tok))
        if score > 0:
            school_results.append((score, school, city, state))
    school_results = sorted(school_results, key=lambda x: x[0], reverse=True)

    print(f'Results for "{query}"')
    if len(school_results) == 0:
        print("No results found")
    else:
        for i, (_, school, city, state) in enumerate(school_results[:3]):
            print(f"{i+1}. {school}\n{city}, {state}")

    # print(f"Search took {time.time() - t} seconds")


if __name__ == "__main__":
    print(*search_schools("elementary school highland park"), sep="\n")
    print("------------------")
    print(*search_schools("jefferson belleville"), sep="\n")
    print("------------------")
    print(*search_schools("riverside school 44"), sep="\n")
    print("------------------")
    print(*search_schools("KUSKOKWIM"), sep="\n")
    print("------------------")
    print(*search_schools("foley high alabama"), sep="\n")
    print("------------------")
    print(*search_schools("granada charter school"), sep="\n")
