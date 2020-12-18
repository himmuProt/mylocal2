import configparser
configParser = configparser.RawConfigParser()
configFilePath = r'/home/proton/Desktop/python/memcached.txt'
configParser.read(configFilePath)
self.path = configParser.get('memcached.txt', '/home/proton/Desktop/python/')