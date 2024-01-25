import os
import re
from os import environ, getenv

class Config(object):

    TECH_VJ_URL = environ.get('TECH_VJ_URL', 'moneykamalo.com') # your shortlink url domain or url without https://
    TECH_VJ_API = environ.get('TECH_VJ_API', '0eefb93e1e3ce9470a7033115ceb1bad13a9d674') # your url shortner api
    
    # channel information
    TECH_VJ_LOG_CHANNEL = int(os.environ.get("TECH_VJ_LOG_CHANNEL", "")) # your log channel id and make bot admin in log channel with full right 
    
