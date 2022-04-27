##################################### Script to interact with Google Pub Sub service ###################################

'''
This is a python script to consume and publish events to google pub sub topics.
'''

########################################################################################################################

### Importing required modules

# 3rd party modules
from google.cloud import pubsub_v1      # Interact with google pub sub service

########################################################################################################################

class PubSub:
    '''
    The class contain methods to pull and push data from and 
    into a google pubsub topic.

    Attributes
    ----------
    '''

    def __init__(self, project_id: str, topic_id: str) -> None:
        '''
        Function to instantiate class objects.
        ...

        Paramters
        ---------
        project_id (str):
            ID of the GCP project
        topic_id (str):
            ID of the pubsub topic

        Returns
        -------
        None
        '''

        self.project = project_id
        self.topic = topic_id


    def publish_data(self, data: str) -> None:
        '''
        Function to publish data to a pubsub topic.
        ...

        Parameters
        ----------
        data (str):
            string to be published in the topic
        '''

        publisher = pubsub_v1.PublisherClient()
        topic_path = publisher.topic_path(self.project, self.topic)

        data = data.encode("utf-8")
        future = publisher.publish(topic_path, data)
        print(future.result())


########################################################################################################################


if __name__ == "__main__":
    ...

