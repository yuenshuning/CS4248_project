from abc import abstractmethod

class BaseModel:
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def train(self, *args, **kwargs):
        """
        TODO
        """
        pass
    
    @abstractmethod
    def summarize(self, *args, **kwargs):
        """
        TODO
        """
        pass
    
