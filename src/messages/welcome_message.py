"""
This module hears to welcome messages. Use it as a example.
"""


class WelcomeMessage:

    def __init__(self, bot):
        self.bot = bot
        self.words = ['hello', 'hi', 'hola', 'que ase', 'que pasa', 'buenas']

    def listenTo(self, channel, message, event):
        return any([word in message.lower() for word in self.words])

    def reactTo(self, channel, message, event):
        self.bot.sendMessage(
            channel, 'Hi my friend, trust me and tell me what to estimate (i.e. estimate UIF-233)')
