import json
import requests

class UpdateFetcher:
    def __init__(self):
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        self.token = config.get('github_token')
        self.headers = {'Authorization': f'token {self.token}'}

    def fetch_updates(self, subscriptions):
        updates = {}
        for repo in subscriptions:
            updates[repo] = self._fetch_repo_updates(repo)
        return updates

    def _fetch_repo_updates(self, repo):
        url = f'https://api.github.com/repos/{repo}/releases/latest'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            release_info = response.json()
            return {
                "tag_name": release_info.get("tag_name"),
                "name": release_info.get("name"),
                "body": release_info.get("body"),
                "published_at": release_info.get("published_at")
            }
        else:
            print(f"Failed to fetch updates for {repo}. Status Code: {response.status_code}")
            return {}