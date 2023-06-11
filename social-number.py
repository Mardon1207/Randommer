import requests
from randommer import Randommer
randomer=Randommer()

class SocialNumber(Randommer):
    def __init__(self,api_key) -> None:
        self.api_key=api_key
    def get_SocialNumber(self) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        
        bese_url=randomer.base_url
        url=bese_url+"SocialNumber"
        haerdes={
            "X-Api-Key":self.api_key
        }
        r=requests.get(url,headers=haerdes)
        return r.json()

key="f1ab06cd2da14928a4f4299e85162d76"
social=SocialNumber(key)
print(social.get_SocialNumber())