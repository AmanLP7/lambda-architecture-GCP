#################################### Script to create a lambda architecture using GCP ##################################

'''
This script creates a lambda architecture to store wikimedia change log data.
'''

########################################################################################################################

### Importing required modules

# System library imports
from datetime import datetime, timedelta        # Python date and time
import sys                                      # System specific functions and parameters

# User defined modules
from query_api import Wikimedia                 # Get wikimedia change log data
from pub_sub import PubSub                      # Interact with google pub sub service
