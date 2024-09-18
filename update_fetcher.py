import os
import requests
import json
from datetime import datetime

class UpdateFetcher:
    def __init__(self):
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        self.token = config.get('github_token')
        self.headers = {'Authorization': f'token {self.token}'}

    def fetch_issues_and_prs(self, repo):
        issues_url = f'https://api.github.com/repos/{repo}/issues'
        prs_url = f'https://api.github.com/repos/{repo}/pulls'
        issues = self._fetch_data(issues_url)
        prs = self._fetch_data(prs_url)
        return issues, prs

    def _fetch_data(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from {url}. Status Code: {response.status_code}")
            return []

    def export_to_markdown(self, repo, issues, prs):
        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f"{repo.replace('/', '_')}_{date_str}.md"
        with open(filename, 'w') as md_file:
            md_file.write(f"# Daily Progress Report for {repo} - {date_str}\n\n")
            md_file.write("## Issues\n")
            for issue in issues:
                md_file.write(f"- [{issue['title']}]({issue['html_url']})\n")
            md_file.write("\n## Pull Requests\n")
            for pr in prs:
                md_file.write(f"- [{pr['title']}]({pr['html_url']})\n")
        print(f"Report exported to {filename}")