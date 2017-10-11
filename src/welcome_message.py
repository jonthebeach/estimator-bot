"""
This module hears to welcome messages. Use it as a example.
"""

class WelcomeMessage:

  def __init__(self, bot):
    self.bot = bot
    self.words = ['hello', 'hi', 'hola', 'que ase', 'que pasa', 'buenas']

  def listenTo(self, from_data, message):
    return any([word in message.lower() for word in self.words])

  def reactTo(self, from_data, message):
    self.bot.sendMessage(from_data, 'Hi my friend, trust me and tell me what to estimate (i.e. estimate UIF-233)')