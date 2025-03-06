import os
from github import Github
from datetime import datetime, timedelta

def list_pull_requests(token, repo_name, start_date_str, end_date_str, output_file="list.log"):
    """
    Lists all pull requests in a repository within a given date range and writes them to a file.

    Args:
        token (str): GitHub personal access token.
        repo_name (str): The repository name (e.g., "owner/repo").
        start_date_str (str): Start date in YYYY-MM-DD format.
        end_date_str (str): End date in YYYY-MM-DD format.
        output_file (str): The name of the output file.
    """
    try:
        g = Github(token)
        repo = g.get_repo(repo_name)

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d") + timedelta(days=1)

        pull_requests = repo.get_pulls(state="all", sort="created", direction="desc")

        with open(output_file, "w") as f:
            for pr in pull_requests:
                if start_date <= pr.created_at <= end_date:
                    f.write(f"{pr.title}\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Use different names for the environment variables
    github_token = os.environ.get("GITHUB_TOKEN")  
    repo_name = os.environ.get("GH_REPOSITORY")

    if not github_token:
        print("Error: GITHUBH_TOKEN environment variables not set.")
        exit(1)
    if not repo_name:
        print("Error: GH_REPOSITORY environment variables not set.")
        exit(1)

    start_date = "2023-01-01"
    end_date = "2023-12-31"

    list_pull_requests(github_token, repo_name, start_date, end_date)
