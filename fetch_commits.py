import requests

# Public GitHub repository (change if needed)
REPO_OWNER = "torvalds"
REPO_NAME = "linux"

# GitHub API URL
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"

def fetch_commits():
    response = requests.get(API_URL)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Fetch the latest 10 commits
            author = commit["commit"]["author"]["name"]
            message = commit["commit"]["message"]
            print(f"Author: {author}\nMessage: {message}\n")
    else:
        print(f"Failed to fetch commits: {response.status_code}")

if __name__ == "__main__":
    fetch_commits()
