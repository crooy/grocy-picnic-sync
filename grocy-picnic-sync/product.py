import json
from .config import Config
from .picnic import PicnicClient

class ProductSync():
     def __init__(self, picnic: PicnicClient):
          self.picnic = picnic;
     
     def __repr__(self) -> str:
        return f"{type(self).__name__}({self.picnic})"

     def search(self, query: str):
          products = self.picnic.searchProduct(query);
          return json.dumps(products, indent=4);