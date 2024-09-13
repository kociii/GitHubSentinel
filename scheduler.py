from apscheduler.schedulers.background import BackgroundScheduler

class Scheduler:
    def __init__(self, subscription_manager, update_fetcher, notifier, report_generator):
        self.subscription_manager = subscription_manager
        self.update_fetcher = update_fetcher
        self.notifier = notifier
        self.report_generator = report_generator
        self.scheduler = BackgroundScheduler()

    def fetch_and_notify(self):
        updates = self.update_fetcher.fetch_updates(self.subscription_manager.get_subscriptions())
        report = self.report_generator.generate_report(updates)
        self.notifier.send_notification(report)

    def start(self):
        # 添加定时任务，每天运行一次
        self.scheduler.add_job(self.fetch_and_notify, 'interval', days=1)
        self.scheduler.start()

    def shutdown(self):
        self.scheduler.shutdown()