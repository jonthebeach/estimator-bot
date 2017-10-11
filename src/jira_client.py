"""
JIRA Client 
"""

from jira import JIRA
from settings import __jira_server__
import os

class JiraClient:
  def __init__(self):
    self.jira_client = JIRA(basic_auth=(os.environ.get('SLACK_BOT_JIRA_USER'), os.environ.get('SLACK_BOT_JIRA_PASS')), server=__jira_server__)
  
  def getIssue(self, id):
    return self.jira_client.issue(id)

if __name__ == "__main__":
  jira_client = JiraClient()
  jira_issue = jira_client.getIssue("UIF-370")
  print(jira_issue.fields.summary, jira_issue.fields.description)
  print(dir(jira_issue.fields))