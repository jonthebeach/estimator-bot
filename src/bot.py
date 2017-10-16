"""
Estimator Slack Bot. Help you estimate Jira user stories easily.
No more unbearable grooming/planning estimation sessions
"""

from slackclient import SlackClient
from messages.welcome_message import WelcomeMessage
from messages.estimation_message import EstimationMessage
from messages.jira_message import JiraMessage
from messages.debug_message import DebugMessage
from messages.excuses_message import ExcusesMessage
from messages.offensive_mode_message import OffeniveModeMessage
from settings import __bot_user_id__
import time
import os


class Bot:

    def __init__(self, token=os.environ.get('SLACK_BOT_TOKEN')):
        self.token = token
        self.slack_client = SlackClient(token)
        self.hearsTo = [WelcomeMessage(self), EstimationMessage(
            self), JiraMessage(self), DebugMessage(self), ExcusesMessage(self), OffeniveModeMessage(self)]

    def gotAMessage(self, event):
        return 'channel' in event and 'text' in event and event.get('type') == 'message'

    def sendMessage(self, to, msg):
        self.slack_client.api_call(
            'chat.postMessage',
            channel=to,
            text=msg,
            as_user=True
        )

    def isNotBotMessage(self, user):
        return user != __bot_user_id__

    def start(self):
        if self.slack_client.rtm_connect():
            while True:
                for event in self.slack_client.rtm_read():
                    if self.gotAMessage(event):
                        channel = event['channel']
                        text = event['text']
                        for subscriber in self.hearsTo:
                            if self.isNotBotMessage(event['user']) and subscriber.listenTo(channel, text, event):
                                subscriber.reactTo(channel, text, event)
                time.sleep(1)
        else:
            print('Connection failed, invalid token?')
