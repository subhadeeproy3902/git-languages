# GitHub Language Usage Analyzer

This script analyzes the most used programming languages in the GitHub repositories of a specified user. It fetches repository data using GitHub's GraphQL API, calculates the size of each language used in the repositories, and displays the results in percentage form.

## Features

- Fetches repository data from GitHub using the GraphQL API.
- Calculates the usage percentage of each programming language across all repositories.
- Displays the most used languages in a clean and simple format.
- Animated loading dots while fetching repository data to enhance user experience.

## Requirements

- Python 3.x
- `requests` library (can be installed via `pip`)

## How to Get a GitHub Token

To access private repositories using the GitHub API, you'll need to create a personal access token with the right permissions. Here's how you can get it:

1. Go to your [GitHub Settings](https://github.com/settings/tokens).
2. Click on **Generate new token**.
3. Select the **repo** scope, which includes access to both public and private repositories.
4. (Optional) You can also select additional scopes like `read:user` if you need to access other parts of your account.
5. Click **Generate token**.
6. Copy the token and store it safely, as it will not be shown again.

Once you have your token, replace `YOUR_GITHUB_TOKEN` in the script with the token you generated.

## Usage

1. Clone the repository and navigate into the project directory.
2. Replace the `YOUR_GITHUB_TOKEN` and `YOUR_GITHUB_USERNAME` variables in the script with your GitHub token and the username you want to analyze.
3. Run the script:
   ```bash
   python languagesused.py
   ```
4. The script will fetch the repository data, calculate the language percentages, and display the results.

## Example Output

```bash
Fetching repositories for subhadeeproy3902...

Most used languages for subhadeeproy3902
TypeScript: 38.02%
HTML: 24.86%
JavaScript: 24.43%
CSS: 8.86%
SCSS: 1.14%
ActionScript: 0.49%
Astro: 0.43%
```
