"""
This module defines common global bot application settings
"""

import ConfigParser

# Read-only Settings

__author__ = "Zuri Pabon"
__copyright__ = ""
__credits__ = []
__license__ = "MITGPL"
__version__ = "1.0.0"
__status__ = "Alpha"

__jira_server__ = "https://pebl.itrsgroup.com"
__bot_user_id__ = "U6ET31TBK"

# Writable Settings

config = ConfigParser.RawConfigParser()
config.add_section('options')
config.set("options", "offensive", True)
