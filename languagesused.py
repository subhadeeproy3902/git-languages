import requests

GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"  # Replace with your GitHub token
USERNAME = "YOUR_GITHUB_USERNAME"  # Replace with the GitHub username you want to analyze

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}

query = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    repositories(first: 100, after: $cursor) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        languages(first: 10) {
          edges {
            size
            node {
              name
            }
          }
        }
      }
    }
  }
}
"""

def fetch_all_repos():
    print(f"Fetching repositories for {USERNAME}...")
    has_next_page = True
    cursor = None
    all_languages = []
    
    while has_next_page:
        variables = {"login": USERNAME, "cursor": cursor}
        response = requests.post(
            "https://api.github.com/graphql",
            json={"query": query, "variables": variables},
            headers=headers
        )

        data = response.json()
        
        if "errors" in data:
            print("Error:", data["errors"])
            break
        
        repos = data["data"]["user"]["repositories"]["nodes"]
        for repo in repos:
            all_languages.extend(repo["languages"]["edges"])

        page_info = data["data"]["user"]["repositories"]["pageInfo"]
        has_next_page = page_info["hasNextPage"]
        cursor = page_info["endCursor"]
    
    return all_languages

def calculate_language_percentages(language_edges):
    language_sizes = {}
    total_size = 0

    for lang in language_edges:
        name = lang["node"]["name"]
        size = lang["size"]
        language_sizes[name] = language_sizes.get(name, 0) + size
        total_size += size

    return {
        lang: round((size / total_size) * 100, 2)
        for lang, size in sorted(language_sizes.items(), key=lambda x: x[1], reverse=True)
    }

# Run the fetch and calculate
all_language_edges = fetch_all_repos()
language_percentages = calculate_language_percentages(all_language_edges)

# Output
print(f"\nMost used languages for {USERNAME}")
for lang, percent in language_percentages.items():
    print(f"{lang}: {percent}%")