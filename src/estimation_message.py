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
    self.words = ['estima']

  def listenTo(self, from_data, message):
    return any([word in message.lower() for word in self.words])

  def getEstimation(self, jira_issue):
    return random.choice(self.story_points)

  def reactTo(self, from_data, message):
    jira_issue_id = message.split(' ')[1]
    jira_issue = self.jira_client.getIssue(jira_issue_id)
    estimation_points = self.getEstimation(jira_issue)
    response_msg = '{0} story points for {1} ({2})!'.format(str(estimation_points), jira_issue_id, jira_issue.fields.summary)   
    self.bot.sendMessage(from_data, response_msg)