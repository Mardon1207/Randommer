import requests
from randommer import Randommer
randomer=Randommer()


class Misc(Randommer):
    def __init__(self,api_key)  :
        self.api_key=api_key
    def get_cultures(self) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        base_url=randomer.base_url      
        url=base_url+"Misc/Cultures"
        heardes={
            "X-Api-Key":self.api_key
        }
        r=requests.get(url,headers=heardes)
        return r.json()
    
    def get_random_address(self,number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        base_url=self.base_url
        url=base_url+"Misc/Random-Address"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "number":number
        }
        r=requests.get(url,params=payload,headers=heardes)
        return r.json()
key="f1ab06cd2da14928a4f4299e85162d76"
misc=Misc(key)
print(misc.get_random_address(1))