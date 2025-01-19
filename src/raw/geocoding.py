import requests
from common.environments import Env


class GeocodingAPI:

    def __init__(self):
        self.params = {
            'q': 'Uberlandia,MG,BR',
            'limit': 1,
            'appid': Env.appid

        }
        self.endpoint = f"{Env.base_url}/geo/1.0/direct"

    def get(self):
        response = requests.get(url=self.endpoint, params=self.params)

        return response.json()



if __name__ == "__main__":
    print(GeocodingAPI().get())
