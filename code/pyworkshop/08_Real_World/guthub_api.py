import requests

GH_REPO_URL = "https://api.github.com/search/repositories"


def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "

    return query


def repos_with_most_star(languages, sort="stars", order="desc"):

    query = create_query(languages)
    PARAMS = {"q": query, "sort": sort, "order": order}
    response = requests.get(GH_REPO_URL, params=PARAMS)

    response_items = response.json()["items"]

    # print("Response from GitHub: ", response.text)
    # print("Keys in response: ", response_json.keys())
    # print("Total Count: ", response_json["total_count"])
    # print("incomplete_results: ", response_json["incomplete_results"])

    return response_items


if __name__ == "__main__":
    languages = ["Python", "Javascript", "C"]
    results = repos_with_most_star(languages)
    # print(results[0])
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"--> {name} is a {language} repo with {stars} stars.")
