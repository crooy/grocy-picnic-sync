import os
from dotenv import load_dotenv

from .config import Config
from .picnic import PicnicClient
from .grocy import GrocyClient
from .product import ProductSync

class GrocyPicnicSync():
    def __init__(self):
        load_dotenv();
        ev = dict(os.environ)
        self.config = Config(ev)
        self.picnic = PicnicClient(self.config.picnic_username, self.config.picnic_password)
        self.grocy = GrocyClient(self.config.grocy_api_key, self.config.grocy_api_host)
        self.product = ProductSync(self.picnic);
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}()"

    def syncProducts(self, query:str):
        return self.product.search(query)
    

