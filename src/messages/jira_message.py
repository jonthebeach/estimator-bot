"""
This module hears to estimation messages and response back to them by using
predictive machine/deep learning
"""
from jira_client import JiraClient

class JiraMessage:

  def __init__(self, bot):
    self.bot = bot
    self.jira_client = JiraClient()
    self.words = [':jira']

  def listenTo(self, channel, message, event):
    return any([word in message.lower() for word in self.words])

  def reactTo(self, channel, message, event):
    jira_issue_id = self.jira_client.getIssueID(message)
    jira_issue = self.jira_client.getIssue(jira_issue_id)
    if jira_issue_id is None or jira_issue is None:
      return self.bot.sendMessage(channel, 'No jira issue found')
    response_msg = 'Summary: {0} \nDescription: {1} \nLabels: {2}\nEstimation: {3}'.format(jira_issue.fields.summary.encode('utf-8').strip(), jira_issue.fields.description.encode('utf-8').strip(), ''.join(str(e).encode('utf-8').strip() for e in jira_issue.fields.labels), str(jira_issue.fields.timeestimate).encode('utf-8').strip())   
    self.bot.sendMessage(channel, response_msg)