
import os

class Config():
    def __init__(self, config):
        self.picnic_username = config['PICNIC_USERNAME']
        self.picnic_password = config['PICNIC_PASSWORD']
        self.grocy_api_key = config['GROCY_API_KEY']
        self.grocy_api_host = config['GROCY_API_HOST']
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}(grocy={self.api_host}, picnic={self.picnic_username})"
