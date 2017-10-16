"""
JIRA Client 
"""

from jira import JIRA
from settings import __jira_server__, config
import re
import os


class JiraClient:
    def __init__(self):
        self.jira_client = JIRA(basic_auth=(os.environ.get(
            'SLACK_BOT_JIRA_USER'), os.environ.get('SLACK_BOT_JIRA_PASS')), server=__jira_server__)

    def getIssue(self, id):
        try:
            return self.jira_client.issue(id)
        except:
            return None

    def getIssueID(self, message):
        matchID = re.search('uif-[0-9]+', message, re.IGNORECASE)
        return None if matchID is None else message[matchID.start():matchID.end()]


if __name__ == "__main__":
    jira_client = JiraClient()
    jira_issue = jira_client.getIssue("UIF-370")
    # print(vars(jira_issue.fields))
    print('Summary: {0} \nDescription: {1} \nLabels: {2}\nEstimation: {3}'.format(jira_issue.fields.summary.encode('utf-8').strip(), jira_issue.fields.description.encode(
        'utf-8').strip(), ''.join(str(e).encode('utf-8').strip() for e in jira_issue.fields.labels), str(jira_issue.fields.timeestimate).encode('utf-8').strip()))
    print(dir(jira_issue.fields))
