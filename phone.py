import requests
from randommer import Randommer
randomer=Randommer()

class Phone(Randommer):
    def __init__(self,api_key) -> None:
        self.api_key=api_key
    def generate(self, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        base_url=randomer.base_url
        url=base_url+"Phone/Generate"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "CountryCode":CountryCode,
            "Quantity":Quantity
        }
        r=requests.get(url,params=payload,headers=heardes)
        return r.json()
    
    def get_IMEI(self, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        base_url=randomer.base_url
        url=base_url+"Phone/IMEI"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "Quantity":Quantity
        }
        r=requests.get(url,params=payload,headers=heardes)
        return r.json()
    
    def is_valid(self, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        base_url=randomer.base_url
        url=base_url+"Phone/Validate"
        heardes={
            "X-Api-Key":self.api_key
        }
        payload={
            "telephone":telephone,
            "CountryCode":CountryCode
        }
        r=requests.get(url,params=payload,headers=heardes)
        return r.json()
    
    def get_countries(self) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        base_url=randomer.base_url
        url=base_url+"Phone/Countries"
        heardes={
            "X-Api-Key":self.api_key
        }
        r=requests.get(url,headers=heardes)
        return r.json()
key="f1ab06cd2da14928a4f4299e85162d76"
phone=Phone(key)
print(phone.get_countries())
