import cmd
from subscription_manager import SubscriptionManager
from update_fetcher import UpdateFetcher
from notifier import Notifier
from report_generator import ReportGenerator
from scheduler import Scheduler
from llm_module import LLMModule
from datetime import datetime


class SentinelShell(cmd.Cmd):
    intro = (
        "Welcome to the GitHub Sentinel shell.\n"
        "Type help or ? to list commands.\n"
        "Available commands:\n"
        "  add owner/repo    : Add a repository subscription\n"
        "  remove owner/repo : Remove a repository subscription\n"
        "  fetch             : Fetch updates for all subscribed repositories\n"
        "  list              : List all subscribed repositories\n"
        "  exit              : Exit the shell\n"
    )
    prompt = "(sentinel) "

    def __init__(self, subscription_manager, update_fetcher, notifier, report_generator):
        super().__init__()
        self.subscription_manager = subscription_manager
        self.update_fetcher = update_fetcher
        self.notifier = notifier
        self.report_generator = report_generator

    def do_add(self, repo):
        "Add a repository subscription: add owner/repo"
        if repo:
            self.subscription_manager.add_subscription(repo)
            print(f"Added subscription: {repo}")
        else:
            print("Usage: add owner/repo")

    def do_remove(self, repo):
        "Remove a repository subscription: remove owner/repo"
        if repo:
            self.subscription_manager.remove_subscription(repo)
            print(f"Removed subscription: {repo}")
        else:
            print("Usage: remove owner/repo")

    def do_fetch(self, arg):
        "Fetch updates for all subscribed repositories"
        for repo in self.subscription_manager.get_subscriptions():
            issues, prs = self.update_fetcher.fetch_issues_and_prs(repo)
            self.update_fetcher.export_to_markdown(repo, issues, prs)
            markdown_filename = f"{repo.replace('/', '_')}_{datetime.now().strftime('%Y-%m-%d')}.md"
            self.report_generator.generate_daily_report(markdown_filename)
        print("Reports generated for all subscribed repositories.")

    def do_list(self, arg):
        "List all subscribed repositories"
        subscriptions = self.subscription_manager.get_subscriptions()
        print("Subscribed repositories:")
        for repo in subscriptions:
            print(f"- {repo}")

    def do_exit(self, arg):
        "Exit the shell"
        print("Exiting...")
        return True

def main():
    subscription_manager = SubscriptionManager()
    update_fetcher = UpdateFetcher()
    notifier = Notifier()
    llm_module = LLMModule()
    report_generator = ReportGenerator(llm_module)

    # 初始化并启动调度器
    scheduler = Scheduler(subscription_manager, update_fetcher, notifier, report_generator)
    scheduler.start()

    # 启动交互式命令行
    try:
        shell = SentinelShell(subscription_manager, update_fetcher, notifier, report_generator)
        shell.cmdloop()
    finally:
        scheduler.shutdown()

if __name__ == "__main__":
    main()