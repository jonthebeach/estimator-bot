"""
Estimator Slack Bot. Help you estimate Jira user stories easily.
No more unbearable grooming/planning estimation sessions
"""

from slackclient import SlackClient
from welcome_message import WelcomeMessage 
from estimation_message import EstimationMessage
from jira_message import JiraMessage
import time
import os

class Bot:

  def __init__(self, token=os.environ.get('SLACK_BOT_TOKEN')):
    self.token = token
    self.slack_client = SlackClient(token)
    self.hearsTo = [WelcomeMessage(self), EstimationMessage(self), JiraMessage(self)]

  def gotAMessage(self, event):
    return 'channel' in event and 'text' in event and event.get('type') == 'message'

  def sendMessage(self, to, msg):
    self.slack_client.api_call(
      'chat.postMessage',
      channel=to,
      text=msg,
      as_user=True
    )

  def start(self):
    if self.slack_client.rtm_connect():
      while True:
        for event in self.slack_client.rtm_read():
          if self.gotAMessage(event):
            channel = event['channel']
            text = event['text']
            for subscriber in self.hearsTo:
              if subscriber.listenTo(channel, text):
                subscriber.reactTo(channel, text)
        time.sleep(1)
    else:
      print('Connection failed, invalid token?')