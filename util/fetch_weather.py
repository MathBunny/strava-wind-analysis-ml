import json
import urllib2
import dateutil.parser
from config import *

class Weather (object):
    _cache = {}

    def __init__(self):
        # Persist the cache in a text file (Redis would be better)
        file  = open("data.txt", "r")
        for line in file:
            if line == '\n':
                continue
            key_val = line.split(' ')
            key = key_val[0]
            val = key_val[1]
            self._cache[key] = val

    def make_request(self, key):
        if key in self._cache:
            return self._cache[key]

        print 'Cache miss for ' + key

        date_str = key.split(',')[2]
        date_obj = dateutil.parser.parse(date_str)
        hour = date_obj.hour

        # Key => ${latitude},${longitude},${date}
        endpoint = "https://api.forecast.io/forecast/{}/{}?units=ca"
        res = json.loads(urllib2.urlopen(endpoint.format(WEATHER_ACCESS_TOKEN,key)).read())['hourly']['data'][hour]
        ret = str(res['windSpeed']) + ',' + str(res['windBearing'])
        self._cache[key] = ret
        return ret

    def close(self):
        file = open("data.txt", "w")
        for key in self._cache:
            file.write(key + ' ' + self._cache[key] + '\n')
        file.close()