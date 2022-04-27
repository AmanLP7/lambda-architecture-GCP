#################################### Script to create a lambda architecture using GCP ##################################

'''
This script creates a lambda architecture to store wikimedia change log data.
'''

########################################################################################################################

### Importing required modules

# System library imports
from datetime import datetime, timedelta        # Python date and time
import sys                                      # System specific functions and parameters

# 3rd party modules
import yaml                                     # Work with YAML files

# User defined modules
from query_api import Wikimedia                 # Get wikimedia change log data
from pub_sub import PubSub                      # Interact with google pub sub service

########################################################################################################################


if __name__ == "__main__":

    # Reading project and topic name
    # from YAML file
    with open("config.yaml", "r") as file:
        try:
            config = yaml.safe_load(file)
            project = config["project_id"]
            topic = config["topic_id"]
        except yaml.YAMLError as exc:
            print(exc)

    wiki = Wikimedia()
    stream = PubSub(project_id=project, topic_id=topic)

    for item in wiki.get_wiki_stream():
        stream.publish_data(item)

