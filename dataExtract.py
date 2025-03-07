import os
from github import Github
from datetime import datetime, timedelta
def list_pull_requests(token, repo_name, start_date_str, end_date_str, output_file="list.log"):
    try:
        g = Github(token)
        repo = g.get_repo(repo_name)

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d") + timedelta(days=1)

        pull_requests = repo.get_pulls(state="all", sort="created", direction="desc")

        print(f"Attempting to create file: {output_file}") #added line.
        with open(output_file, "w") as f:
            print(f"File {output_file} created.") #added line.
            for pr in pull_requests:
                if start_date <= pr.created_at <= end_date:
                    f.write(f"{pr.title}\n")
                    print(f"Wrote PR: {pr.title}") #added line.
        print(f"File {output_file} writing finished.") #added line.

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
    end_date = "2025-12-31"

    list_pull_requests(github_token, repo_name, start_date, end_date)
