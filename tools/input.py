import os
import requests as req
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


class Input:
    def __init__(self, year, day, cacheFile):
        self.year = year;
        self.day = day;
    
    def getFromSource(self, url):
        data = req.get(url, cookies={
            'session': os.getenv("SESSION_COOKIE")})
        return data;

    def createURL(self):
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        return url;

    def doesExistInCache()
