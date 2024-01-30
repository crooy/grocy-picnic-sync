from python_picnic_api import PicnicAPI

class PicnicClient():
    def __init__(self, username, password):
        self.username = username
        self.client = PicnicAPI(username=username, password=password, country_code="NL")

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.username})"
    
    def searchProduct(self, query):                
        return list(filter( lambda p: p.get('type') == 'SINGLE_ARTICLE', self.client.search(query)[0]['items']));
