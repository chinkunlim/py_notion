# import libraries
import os
import configparser

# import modules

class Config:
    def __init__(self, ini_path="config.ini"):
        self.config=configparser.ConfigParser()
        if os.path.exists(ini_path):
            self.config.read(ini_path, encoding="utf-8")

    def get_config(self, key, section, default):
        if section and self.config.has_option(section, key):
            return self.config.get(section, key)
        return default

config = Config()