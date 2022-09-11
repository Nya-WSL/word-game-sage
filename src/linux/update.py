import zipfile
import urllib.request
from urllib import request
from configparser import ConfigParser

def check_update():
    LocalConfig = ConfigParser()
    LocalConfig.read('version.ini')
    File = LocalConfig.get('params', 'version')