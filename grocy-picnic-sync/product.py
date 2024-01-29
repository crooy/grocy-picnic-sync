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
          return list(map(lambda p: f"{p['id']} : {p['name']} {p['unit_quantity']} = {p['price']/100} EURO", products));