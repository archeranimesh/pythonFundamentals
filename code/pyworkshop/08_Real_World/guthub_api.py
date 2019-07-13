import requests

GH_REPO_URL = "https://api.github.com/search/repositories"
PARAMS = {"q": "stars:>50000"}


def repos_with_most_star():
    response = requests.get(GH_REPO_URL, params=PARAMS)
    print("Response from GitHub: ", response.text)


if __name__ == "__main__":
    repos_with_most_star()
