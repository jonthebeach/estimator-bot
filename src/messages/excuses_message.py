"""
This module hears to estimation messages and response back to them by using
predictive machine/deep learning
"""
from jira_client import JiraClient
import random


class ExcusesMessage:

    def __init__(self, bot):
        self.bot = bot
        self.words = [':excuse']
        self.excuses = ["What about security?", "Consider caching issues", "Browser compatibility may be a concern", "documentation can be hard to write", "It might require a hard work at the integration level",
                        "Accesibility has to be taken into account", "It might require to reinvent the wheel", "Have you consider making a POC?", "Scaffolding is required?"]

    def listenTo(self, channel, message, event):
        return any([word in message.lower() for word in self.words])

    def reactTo(self, channel, message, event):
        self.bot.sendMessage(channel, random.choice(self.excuses))
