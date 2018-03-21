from config import *
import json, ast
import urllib2

segments = []

contents = urllib2.urlopen("https://www.strava.com/api/v3/athlete/activities?include_all_efforts=true&per_page=200&access_token=" + ACCESS_TOKEN).read()
data = json.loads(contents)

def get_activities():
    for activity in data:
        print activity["name"]

def get_fields():
    for field in data[0]:
        print field,

def output_activities():
    for activity in data:
        print activity["name"], activity["id"]

def populate_segments():
    for activity in data:
        if activity["type"] != "Ride" or activity["manual"] == True:
            continue
        for segment in activity["segment_efforts"]:
            if segment["id"] not in segments:
                segments.append(segment["id"])
                print segment["id"]


# output_activities()
populate_segments()