import json
from .config import Config
from .picnic import PicnicClient

class ProductSync():     

     def __init__(self, picnic: PicnicClient):
          self.picnic = picnic;
     
     def __repr__(self) -> str:
        return f"{type(self).__name__}({self.picnic})"

     def search(self, query: str):
          self.last_product_search = self.picnic.searchProduct(query);          

     def getSearchSummary(self):
          return list(map(lambda p: f"{p['id']} : {p['name']} {p['unit_quantity']} = {(p.get('price', 1))/100} EURO", self.last_product_search));          

     def getProductFromSearch(self, id: str):
          for item in self.last_product_search:               
               if item['id'] == id:                    
                    return item;                              