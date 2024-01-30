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

    def searchProducts(self, query:str):
        self.product.search(query);
        return self.product.getSearchSummary();
    
    def syncProduct(self, id:str):
        # todo: converteer product en upload in grocy
        return self.product.getProductFromSearch(id);
    

