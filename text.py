import requests
from randommer import Randommer
randomer=Randommer()

class Text(Randommer):
    def __init__(self,api_key) -> None:
        self.api_key=api_key
    def generate_LoremIpsum(self, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        base_url=randomer.base_url
        url=base_url+"Text/LoremIpsum"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "loremType":loremType,
            "type":type,
            "number":number
        }
        r=requests.get(url,params=payload,headers=heardes)
        return r.json()
    
    def generate_password(self, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        pass
key="f1ab06cd2da14928a4f4299e85162d76"
text=Text(key)
print(text.generate_LoremIpsum("normal","words",32))