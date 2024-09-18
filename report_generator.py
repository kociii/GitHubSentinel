import logging

class ReportGenerator:
    def __init__(self, llm_module):
        self.llm_module = llm_module
        logging.basicConfig(level=logging.INFO)

    def generate_daily_report(self, markdown_filename):
        print('进来了4')
        try:
            with open(markdown_filename, 'r') as md_file:
                markdown_content = md_file.read()

            summary = self.llm_module.summarize_report(markdown_content)

            report_filename = markdown_filename.replace('.md', '_summary.md')
            with open(report_filename, 'w') as report_file:
                report_file.write(summary)

            logging.info(f"Summary report generated: {report_filename}")
        except Exception as e:
            logging.error(f"Error generating daily report: {e}")