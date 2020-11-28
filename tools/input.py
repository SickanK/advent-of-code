import os
import requests as req
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)


class Input:
    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.inputCachePath = join(dirname(__file__), '../inputCache/')

    # Check if Cache file exists
    def __doesExistInCache(self):
        if(not os.path.isdir(self.inputCachePath)):
            return -1
        else:
            if(os.path.isfile(join(self.inputCachePath, f'{os.getenv("SESSION_COOKIE")}.txt'))):
                return 1
            else:
                return 0

    # Creates cache file with SESSION_COOKIE env variable as name
    # if cache doesn't exist
    def __createInputCache(self):
        cacheFileStatus = self.__doesExistInCache()
        cacheFile = ""
        if(cacheFileStatus == -1):
            os.mkdir(self.inputCachePath)

        if(cacheFileStatus != 1):
            cacheFile = open(join(self.inputCachePath,
                                  f'{os.getenv("SESSION_COOKIE")}.txt'), "w+")
        return cacheFile

    # Open cache file with the mode: @mode
    def __openCacheFile(self, mode):
        cacheFile = open(
            join(self.inputCachePath, f'{os.getenv("SESSION_COOKIE")}.txt'), f'{mode}')
        return cacheFile

    # Create a URL based on the year and day
    def __createURL(self):
        url = f'https://adventofcode.com/{self.year}/day/{self.day}/input'
        return url

    # Fetch data from server
    def __getFromSource(self, url):
        data = req.get(url, cookies={
            'session': os.getenv("SESSION_COOKIE")})
        data = data.text.split("\n")
        data = ",".join(data)
        return data

    # Get the data from cache
    def __getFromCache(self, url):
        cacheFile = self.__openCacheFile("+r")
        data = cacheFile.read()
        dataArr = data.split("start_of_input\n")[1::]
        for d in dataArr:
            formatedData = d.split("\n")[::-1][1::][::-1]
            if(formatedData[0] == url):
                return formatedData[1]
        return -1

    # Writes @message to cache
    def __writeToCache(self, message):
        cacheFile = self.__openCacheFile("+a")
        cacheFile.write(f'\n{message}')
        return cacheFile

    # if needed: create cache file
    # if exist: gets data from cache
    # if needed: fetches data from server and writes it to cache

    def getData(self):
        self.__createInputCache()
        url = self.__createURL()
        cacheData = self.__getFromCache(url)

        if(cacheData == -1):
            data = self.__getFromSource(url)
            self.__writeToCache(f'start_of_input\n{url}\n{data}\n')
            return data

        return cacheData
