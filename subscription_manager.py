class SubscriptionManager:
    def __init__(self):
        # 初始化订阅列表
        self.subscriptions = ['langchain-ai/langchain']

    def get_subscriptions(self):
        # 返回当前的订阅列表
        return self.subscriptions

    def add_subscription(self, repo_url):
        # 添加新的订阅
        self.subscriptions.append(repo_url)

    def remove_subscription(self, repo_url):
        # 移除订阅
        self.subscriptions.remove(repo_url)