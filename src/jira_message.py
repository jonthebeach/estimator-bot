"""
This module hears to estimation messages and response back to them by using
predictive machine/deep learning
"""
from jira_client import JiraClient

class JiraMessage:

  def __init__(self, bot):
    self.bot = bot
    self.jira_client = JiraClient()
    self.words = ['jira']

  def listenTo(self, from_data, message):
    return any([word in message.lower() for word in self.words])

  def reactTo(self, from_data, message):
    jira_issue_id = message.split(' ')[1]
    jira_issue = self.jira_client.getIssue(jira_issue_id)
    response_msg = 'Summary: {0} | Description: {1})!'.format(jira_issue.fields.summary, jira_issue.fields.description)   
    self.bot.sendMessage(from_data, response_msg)