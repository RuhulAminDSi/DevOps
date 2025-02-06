import requests

# Public GitHub repository
REPO_OWNER = "RuhulAminDSi"
REPO_NAME = "DevOps"

# GitHub API URL
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"

def fetch_commits():
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        commits = response.json()
        commit_list = []
        for commit in commits[:10]:  # Fetch the latest 10 commits
            author = commit["commit"]["author"]["name"]
            message = commit["commit"]["message"]
            commit_list.append({"author": author, "message": message})
        return commit_list  # Return the list of commit data
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        return []  # Return an empty list if the request fails

if __name__ == "__main__":
    print(fetch_commits())  # Print the result to verify
