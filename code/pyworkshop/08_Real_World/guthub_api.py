import requests

GH_REPO_URL = "https://api.github.com/search/repositories"
PARAMS = {"q": "stars:>50000"}


def repos_with_most_star():
    response = requests.get(GH_REPO_URL, params=PARAMS)

    response_items = response.json()["items"]

    # print("Response from GitHub: ", response.text)
    # print("Keys in response: ", response_json.keys())
    # print("Total Count: ", response_json["total_count"])
    # print("incomplete_results: ", response_json["incomplete_results"])

    return response_items


if __name__ == "__main__":
    results = repos_with_most_star()
    # print(results[0])
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"--> {name} is a {language} repo with {stars} stars.")
