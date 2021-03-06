import json

import uuid


class Settings:
    """
    This settings config can be used to retrieve settings from the config.json file.
    """

    def __init__(self):
        """
        Initialize the settings class with the config.json file.
        """
        try:
            with open('local.config.json') as config_file:
                self.config = json.load(config_file)
        except:
            with open('config.json') as config_file:
                self.config = json.load(config_file)

        # initialize variables
        self.SECRET_KEY = self.config['SECRET_KEY']
        self.ADMIN_USER = self.config['ADMIN_USER']
        self.ADMIN_PASSWORD = self.config['ADMIN_PASSWORD']
        self.API_PREFIX = self.config["API_PREFIX"]
        try:
            self.HEADERS = self.config['HEADERS']
        except:
            self.HEADERS = {}

    SECRET_KEY: str
    ADMIN_USER: str
    ADMIN_PASSWORD: str
    API_PREFIX: str

    HEADERS: dict

    def assemble_headers(self):
        return {"ETag": str(uuid.uuid4()), **self.HEADERS}
