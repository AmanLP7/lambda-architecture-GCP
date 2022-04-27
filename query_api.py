###################################### Module to query API data from movie database ####################################

'''
This script interacts with movie data API and queries data.
'''


########################################################################################################################

### Importing required modules

# System library imports
import json                 # Handling JSON data
from time import sleep      # Suspend execution

# 3rd party modules
import requests             # Make HTTP requests
import yaml                 # interact with yaml files


########################################################################################################################

class Wikimedia:
    '''
    Class containing functions to quuery wikimedia 
    change stream.
    ...

    Attributes
    ----------
    stream_url (str): 
        URL used to get the data
    '''

    def __init__(self, URL: str = "https://stream.wikimedia.org/v2/stream/recentchange") -> None:
        '''
        Function to create and instance of the class.
        ...

        Parameters
        ----------
        URL (str):
            URL to be used to pull data

        Returns
        -------
        None
        '''

        self.stream_url = URL


    def get_wiki_stream(self) -> None:
        '''
        Function to get stream of wiki change data.
        ...

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''

        with requests.get(self.stream_url, headers=None, stream=True) as res:
            for line in res.iter_lines():
                sleep(0.5)
                if b'data' in line:
                    line = line.decode("utf8")[6:]
                    line = json.dumps(line)
                    yield line
        

########################################################################################################################


if __name__ == "__main__":

    wiki = Wikimedia()

    wiki.get_wiki_stream()