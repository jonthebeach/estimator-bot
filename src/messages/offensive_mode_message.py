"""
This module hears to estimation messages and response back to them by using
predictive machine/deep learning
"""
from settings import config


class OffeniveModeMessage:

    def __init__(self, bot):
        self.words = [':offensive']

    def listenTo(self, channel, message, event):
        return any([word in message.lower() for word in self.words])

    def reactTo(self, channel, message, event):
        mode = message.split(' ')[-1]
        config.set("options", "offensive", True) if mode.lower(
        ) == "on" else config.set("options", "offensive", False)
