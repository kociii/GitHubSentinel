class ReportGenerator:
    def __init__(self):
        pass

    def generate_report(self, updates):
        # 生成报告的逻辑
        report = "GitHub Updates Report\n"
        for repo, update in updates.items():
            report += f"Repo: {repo}\n"
            if update:
                report += f"Latest Release: {update.get('name', 'N/A')} ({update.get('tag_name', 'N/A')})\n"
                report += f"Published at: {update.get('published_at', 'N/A')}\n"
                report += f"Description: {update.get('body', 'No description')}\n"
            else:
                report += "No release information available.\n"
            report += "\n"
        return report