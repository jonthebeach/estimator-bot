"""
This module hears to estimation messages and response back to them by using
predictive machine/deep learning
"""
from jira_client import JiraClient

class DebugMessage:

  def __init__(self, bot):
    self.bot = bot
    self.jira_client = JiraClient()
    self.words = [':debug']

  def listenTo(self, channel, message, event):
    return any([word in message.lower() for word in self.words])

  def reactTo(self, channel, message, event):
    jira_issue_id = self.jira_client.getIssueID(message)
    jira_issue = self.jira_client.getIssue(jira_issue_id)
    if jira_issue_id is None or jira_issue is None:
      return self.bot.sendMessage(channel, 'No jira issue found')
    response_msg = '{0}'.format(vars(jira_issue.fields))   
    self.bot.sendMessage(channel, response_msg)