"""
Run the bot from the command line
$> SLACK_BOT_TOKEN=<token> SLACK_BOT_JIRA_USER=<jira_username> SLACK_BOT_JIRA_PASS=<jira_password> python src/main.py
"""
from bot import Bot
import settings

if __name__ == "__main__":
  print("Running bot v{0} ...".format(settings.__version__))
  Bot().start()