class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self, updates):
        # 生成报告的逻辑
        report = "GitHub Updates Report\n"
        for repo, update in updates.items():
            report += f"Repo: {repo}\n"
            report += f"Commits: {len(update['commits'])}\n"
            report += f"Issues: {len(update['issues'])}\n"
            report += f"Pull Requests: {len(update['pull_requests'])}\n"
            report += "\n"
        return report
