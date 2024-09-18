import openai
import json
import logging

class LLMModule:
    def __init__(self):
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        self.api_key = config.get('openai_api_key')
        self.client = openai.OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com/v1")
        logging.basicConfig(level=logging.INFO)

    def summarize_report(self, markdown_content):
        logging.info('Entered summarize_report')
        try:
            prompt = f"以下是一个github开源项目的进展，总结项目形成一份简报，简报以中文输出，输出结果需要合并同类项，至少包含：1）新增功能；2）主要改进；3）修复问题；\n\n{markdown_content}"
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "user", "content": prompt}
                ],
            )
            logging.info('Received response from OpenAI')
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Error during OpenAI API call: {e}")
            return "Failed to generate summary."
    