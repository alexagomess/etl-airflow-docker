from os import getenv

class Env:
    appid = getenv('APPID')
    base_url = getenv('BASE_URL')