import requests
from common.environments import Env
from raw.geocoding import GeocodingAPI


class CurrentWeatherApi:

    def __init__(self):
        self.base_url = Env.base_url
        self.endpoint = 'data/2.5/weather'


    def __build_parameters(self):
        geocoding_response = GeocodingAPI().get()
        latitude = geocoding_response[0]['lat']
        longitude = geocoding_response[0]['lon']
        params = {
            'lat': latitude,
            'lon':  longitude,
            'appid': Env.appid
        }
        return params

    def get(self):
        response = requests.get(f"{self.base_url}/{self.endpoint}", params=self.__build_parameters())

        return response.json()
    
    # def save_data(self):


if __name__ == "__main__":
    print(CurrentWeatherApi().get())
