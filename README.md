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

## Usage

1. Clone the repository and navigate into the project directory.
2. Replace the `GITHUB_TOKEN` and `USERNAME` variables in the script with your GitHub token and the username you want to analyze.
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
