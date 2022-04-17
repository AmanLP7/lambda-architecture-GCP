##################################### Script to determine execution time of a function #################################

'''
This is a python script to calculate execution time of a function.
'''

########################################################################################################################

### Importing required modules

# System library imports
from datetime import datetime, timedelta        # Date time functions using python

########################################################################################################################

class GetExecutionTime:
    '''
    Class containing method to get execution time
    of a function.
    ...

    Attributes
    ----------
    func (callable):
        a python function
    '''

    def __init__(self, func: callable) -> None:
        '''
        Function to instantiate
        a class object.
        ...

        Parameters
        ----------
        func (callable):
            a python function

        Returns
        -------
        None
        '''

        self.func = func


    def __call__(self, *args) -> None:
        '''
        Make instance behave like a function,
        and prints its execution time.
        ...

        Parameters
        ----------
        *args (str, int, float):
            arguements can be anythning.

        Returns
        -------
        None
        '''

        start = datetime.now()
        self.func(*args)
        print(f"Execution time for '{self.func.__name__}' = {datetime.now()-start}")

        return None


########################################################################################################################


if __name__ == "__main__":

    ...


