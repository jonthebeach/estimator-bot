"""
This module hears to estimation messages and response back to them by using
predictive machine/deep learning
"""
from jira_client import JiraClient
import random

class EstimationMessage:

  def __init__(self, bot):
    self.bot = bot
    self.jira_client = JiraClient()
    self.story_points = [1, 2, 3, 5, 8]
    self.words = [':estima','estima']

  def listenTo(self, channel, message, event):
    return any([word in message.lower() for word in self.words])

  def getEstimation(self, jira_issue):
    return random.choice(self.story_points)

  def reactTo(self, channel, message, event):
    jira_issue_id = self.jira_client.getIssueID(message)
    jira_issue = self.jira_client.getIssue(jira_issue_id)
    if jira_issue_id is None or jira_issue is None:
      return self.bot.sendMessage(channel, 'No jira issue found')
    estimation_points = self.getEstimation(jira_issue)
    response_msg = '{0} story points for {1} ({2})!'.format(str(estimation_points), jira_issue_id, jira_issue.fields.summary)   
    self.bot.sendMessage(channel, response_msg)