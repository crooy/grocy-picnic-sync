from pygrocy import Grocy

class GrocyClient():
    def __init__(self, api_key: str, api_host: str):
        self.api_host = api_host        
        self.client = Grocy(api_host, api_key)
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.api_host})"
    
    
    
