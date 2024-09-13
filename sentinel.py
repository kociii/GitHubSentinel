from subscription_manager import SubscriptionManager
from update_fetcher import UpdateFetcher
from notifier import Notifier
from report_generator import ReportGenerator

def main():
    # 初始化各个模块
    subscription_manager = SubscriptionManager()
    update_fetcher = UpdateFetcher()
    notifier = Notifier()
    report_generator = ReportGenerator()

    # 获取订阅的仓库列表
    subscriptions = subscription_manager.get_subscriptions()

    # 获取更新
    updates = update_fetcher.fetch_updates(subscriptions)

    # 生成报告
    report = report_generator.generate_report(updates)

    # 发送通知
    notifier.send_notification(report)

if __name__ == "__main__":
    main()
